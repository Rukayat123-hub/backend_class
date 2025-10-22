from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name": "Sam Lary",
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        self.send_data(data)


def run():
    print("Application is running on http://localhost:8000")
    server = HTTPServer(('localhost', 8000), BasicAPI)
    server.serve_forever()


if __name__ == "__main__":
    run()
