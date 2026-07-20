from http.server import BaseHTTPRequestHandler, HTTPServer
import sys


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

    def log_message(self, format, *args):
        sys.stdout.write("%s - - [%s] %s\n" % (
            self.address_string(),
            self.log_date_time_string(),
            format % args,
        ))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()
