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

    def do_DELETE(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        request_data = json.loads(body)
        record_id = request_data.get("id")

        for item in data:
            if item["id"] == record_id:
                data.remove(item)
                self.send_data({"message": f"Record with id {record_id} deleted"}, 200)
                return

        self.send_data({"error": "Record not found"}, 404)

def run():
    print("✅ DELETE API running on http://localhost:8000")
    server = HTTPServer(("localhost", 8000), BasicAPI)
    server.serve_forever()

if __name__ == "__main__":
    run()
