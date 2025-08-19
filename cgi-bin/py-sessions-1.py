#!/usr/bin/env python3
import os, sys, urllib.parse, html
from _py_session_util import load_session, save_session
headers = ["Cache-Control: no-cache", "Content-Type: text/html; charset=UTF-8"]
sid, data, path = load_session(os.environ, headers)
length = int(os.environ.get("CONTENT_LENGTH","0") or 0)
if length>0:
    body = sys.stdin.read(length)
    params = urllib.parse.parse_qs(body, keep_blank_values=True)
    name = params.get("username", [""])[0]
    if name:
        data["username"] = name
        save_session(path, data)
print("\n".join(headers) + "\n")
name = data.get("username","")
print("<!doctype html><html><head><title>Python Sessions Page 1</title></head><body>")
print("<h1 align='center'>Python Sessions Page 1</h1><hr/>")
if name:
    print(f"<p><b>Name:</b> {html.escape(name)}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")
print("""<br/>
<a href="/cgi-bin/py-sessions-2.py">Session Page 2</a><br/>
<a href="/hw2/py/py-cgiform.html">Python CGI Form</a><br/>
<form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
  <button type="submit">Destroy Session</button>
</form>
</body></html>""")
