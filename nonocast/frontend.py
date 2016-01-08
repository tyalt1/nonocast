# Copyright 2016 Tyler Alterio, YuetLong Leung, Matthew Wolf, Allison Ober
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

.table { display: table;}
.cell  { display: table-cell; position: block;
         vertical-align: middle; text-align: center; }

body
{
    position: absolute;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background: url(bg.jpg) no-repeat center center fixed;
    background-size: cover;
}

p { line-height: 0; }

.header
{
    font-family: sans-serif;
    font-size: 3em;
    font-weight: bold;
    color: black;
}

.nono
{
    color: white;
}


button
{
    font-size: 1.5em;
}

        </style>
        <script type="text/javascript">

// in the future we should be doing this all with ajax, not totally hacky
// url params

window.onload = function()
{
    if (window.location.search != '')
        window.location.search = ''
}

        </script>
    </head>
    <body class="table">

<div class="cell">
    <p class="header"><span class="nono">nono</span>cast</p>
    <form action='/'>
        <p><input method="post" name="url"></p>
        <p><button>Rock it!</button></p>
    </form>
</div>

    </body>
</html>
'''

frontend_url_handler = None

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/bg.jpg':
            self.send_response(200)
            self.send_header('content-type', 'image/jpeg')
            self.end_headers()
            bg = open('bg.jpg', 'rb')
            self.wfile.write(bg.read())
            bg.close()
            self.wfile.close()

        else:        
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
        ('', 8000),
        RequestHandler
    )
    while 1:
        server.handle_request()

def handle_url(url):
    print(url)

if __name__ == "__main__":
    run(handle_url)
