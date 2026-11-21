"""A tiny standard-library web app for the vibe-coding lab."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def response_for(path: str) -> tuple[int, str, str]:
    """Return (status, content_type, body) for a request path."""
    if path == "/healthz":
        return 200, "application/json; charset=utf-8", json.dumps({"status": "ok"})
    if path == "/":
        body = """<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Vibe Coding Lab</title>
<body style="font: 1.1rem system-ui; max-width: 48rem; margin: 3rem auto; padding: 0 1rem">
<h1>我的第一个 GitOps 应用</h1>
<p>这段文字正在本机 kind Kubernetes 集群中运行。</p>
<p>试试 <code>/healthz</code> 健康检查接口。</p>
</body></html>"""
        return 200, "text/html; charset=utf-8", body
    return 404, "application/json; charset=utf-8", json.dumps({"error": "not found"})


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, content_type, body = response_for(self.path.split("?", 1)[0])
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    print("Listening on 0.0.0.0:8080")
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
