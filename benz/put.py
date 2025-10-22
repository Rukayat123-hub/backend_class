from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Sample data
data = [
    {
        "id": 1,
        "name": "Sam Lary",
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_PUT(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        updated_item = json.loads(body)

        # Find and update the record
        for item in data:
            if item["id"] == updated_item.get("id"):
                item.update(updated_item)
                self.send_data({
                    "message": "Record updated successfully",
                    "data": item
                }, 200)
                return

        # If no record found
        self.send_data({"error": "Record not found"}, 404)


def run():
    print("✅ PUT API running on http://localhost:8000")
    server = HTTPServer(("localhost", 8000), BasicAPI)
    server.serve_forever()


if __name__ == "__main__":
    run()
