from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"id": 1, "name": "Sam Lary", "track": "AI Developer"},
    {"id": 2, "name": "Jane Doe", "track": "Frontend Developer"}
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_PATCH(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        update = json.loads(body)

        for item in data:
            if item["id"] == update.get("id"):
                item.update(update)
                self.send_data({
                    "message": "Record partially updated",
                    "data": item
                }, 200)
                return

        self.send_data({"error": "Record not found"}, 404)

def run():
    print("✅ PATCH API running on http://localhost:8000")
    server = HTTPServer(("localhost", 8000), BasicAPI)
    server.serve_forever()

if __name__ == "__main__":
    run()
