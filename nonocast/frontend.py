# Copyright 2016 Tyler Alterio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from sys import version_info
import re

if version_info[0] == 2:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from urllib2 import unquote
else:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib3 import unquote

page = '''
<html>
    <head>
        <style type="text/css">
.center { text-align: center; }
input, button { width: 300px; }
        </style>
    </head>
    <body class="center">
        <form action='/'>
            <input method="post" name="url"><br>
            <button>Rock it</button>
        </form>
    </body>
</html>
'''

frontend_url_handler = None

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = re.findall('''\?url=(.*);?''', self.path)

        self.send_response(200)
        if len(params) > 0:
            frontend_url_handler(unquote(params[0]))
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(page)
        self.wfile.close()

def run(handler):
    global frontend_url_handler

    frontend_url_handler = handler
    server = HTTPServer(
        ('localhost', 8000),
        RequestHandler
    )
    while 1:
        server.handle_request()

def handle_url(url):
    print(url)

if __name__ == "__main__":
    run(handle_url)
