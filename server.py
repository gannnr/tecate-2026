# Tecate 2026 local dashboard for Pythonista
# Put this file in the same folder as index.html and tap Run.

import http.server
import socketserver
import os
import threading
import webbrowser

PORT = 8000
FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(FOLDER)

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def open_safari():
    webbrowser.open("http://127.0.0.1:%d/index.html" % PORT)

print("Tecate 2026 dashboard")
print("Serving:", FOLDER)
print("Opening Safari at http://127.0.0.1:%d" % PORT)
print("Keep Pythonista running while you use the page.")
print("Stop the server with the square Stop button in Pythonista.")

threading.Timer(0.8, open_safari).start()

with ReusableTCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
