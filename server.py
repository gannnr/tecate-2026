# Draft Companion local server for Pythonista
# v29 - disables Safari caching.

import http.server
import socketserver
import os
import threading
import webbrowser
import time

PORT = 8000
FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(FOLDER)

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

VERSION = "29"
URL = "http://127.0.0.1:%d/index.html?v=%s&t=%d" % (
    PORT, VERSION, int(time.time())
)

def open_safari():
    webbrowser.open(URL)

print("Draft Companion v29")
print("Serving:", FOLDER)
print("Opening:", URL)
print("Browser cache disabled.")

threading.Timer(0.8, open_safari).start()

with ReusableTCPServer(("127.0.0.1", PORT), NoCacheHandler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
