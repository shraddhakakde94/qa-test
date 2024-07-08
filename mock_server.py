from http.server import BaseHTTPRequestHandler, HTTPServer

class MockServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/up':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Application is UP')
        elif self.path == '/down':
            self.send_response(503)  # Service Unavailable
            self.end_headers()
            self.wfile.write(b'Application is DOWN')
        else:
            self.send_response(404)  # Not Found
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')

def run_mock_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MockServerHandler)
    print('Mock server is running at http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_mock_server()
