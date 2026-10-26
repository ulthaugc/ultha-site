# Local preview with clean URLs (like Vercel): python3 tools/serve.py  ->  http://localhost:8794
import http.server, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def send_head(s):
        p = s.path.split('?')[0]
        fs = os.path.join(ROOT, p.lstrip('/'))
        if not os.path.exists(fs) and os.path.exists(fs.rstrip('/') + '.html'):
            s.path = p.rstrip('/') + '.html'
        return super().send_head()
    def log_message(s, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', 8794), H).serve_forever()
