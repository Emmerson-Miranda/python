import http.server
import socketserver
import logging
import sys
from http import HTTPStatus
from datetime import datetime


class Handler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler"""

    def do_GET(self):
        """handling GET method"""
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        now = datetime.now() 
        msg = 'Hello world ' + now.strftime("%d/%m/%Y, %H:%M:%S" + " !")
        self.wfile.write(bytes(msg, encoding="utf8"))
        logging.info('Get call - served')

# configuring logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# determinating port
port = 8080
if(len(sys.argv) == 2):
  port = int(sys.argv[1])

# starting server
httpd = socketserver.TCPServer(('', port), Handler)
logging.info('Server started ' + str(port))
httpd.serve_forever()