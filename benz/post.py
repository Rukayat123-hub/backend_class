from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"id": 1, "name": "Sam Lary", "track": "AI Developer"}
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        new_item = json.loads(body)

        new_item["id"] = len(data) + 1
        data.append(new_item)

        self.send_data({
            "message": "Record created successfully",
            "data": new_item
        }, 201)

def run():
    print("✅ POST API running on http://localhost:8000")
    server = HTTPServer(("localhost", 8000), BasicAPI)
    server.serve_forever()

if __name__ == "__main__":
    run()
