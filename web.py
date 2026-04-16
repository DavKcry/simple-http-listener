import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"\n[+] GET Request received")
        if 'data=' in self.path:
            try:
                query = urllib.parse.urlparse(self.path).query
                print(f"RAW: {query}")
            except:
                pass
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        print(f"\n[+] POST Request received")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"DATA: {post_data}")
        self.send_response(200)
        self.end_headers()

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f"Serving on port {port}...")
httpd.serve_forever()
