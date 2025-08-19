#!/usr/bin/env python3
import os, html
from _py_session_util import load_session
headers = ["Cache-Control: no-cache", "Content-Type: text/html; charset=UTF-8"]
sid, data, path = load_session(os.environ, headers)
print("\n".join(headers) + "\n")
name = data.get("username","")
print("<!doctype html><html><head><title>Python Sessions Page 2</title></head><body>")
print("<h1 align='center'>Python Sessions Page 2</h1><hr/>")
if name:
    print(f"<p><b>Name:</b> {html.escape(name)}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")
print("""<br/>
<a href="/cgi-bin/py-sessions-1.py">Session Page 1</a><br/>
<a href="/hw2/py/py-cgiform.html">Python CGI Form</a><br/>
<form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
  <button type="submit">Destroy Session</button>
</form>
</body></html>""")
