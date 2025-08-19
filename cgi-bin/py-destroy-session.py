#!/usr/bin/env python3
import os, time
from _py_session_util import load_session
headers = ["Cache-Control: no-cache", "Content-Type: text/html; charset=UTF-8"]
sid, data, path = load_session(os.environ, headers)
# 清 cookie
headers.append("Set-Cookie: CGISESSID=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT")
# 删文件
try:
    if os.path.exists(path): os.remove(path)
except: pass
print("\n".join(headers) + "\n")
print("""<!doctype html><html><head><title>Python Session Destroyed</title></head><body>
<h1>Session Destroyed</h1>
<a href="/hw2/py/py-cgiform.html">Back to the Python CGI Form</a><br />
<a href="/cgi-bin/py-sessions-1.py">Back to Page 1</a><br />
<a href="/cgi-bin/py-sessions-2.py">Back to Page 2</a>
</body></html>""")
