import os, sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import re, urllib2

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
            frontend_url_handler(urllib2.unquote(params[0]))
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
    print url
run(handle_url)
