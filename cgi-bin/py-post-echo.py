#!/usr/bin/env python3
import os, sys, urllib.parse, html
print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=UTF-8\n")
length = int(os.environ.get("CONTENT_LENGTH","0") or 0)
body = sys.stdin.read(length) if length>0 else ""
params = urllib.parse.parse_qs(body, keep_blank_values=True)
print("<!doctype html><html><head><title>Python POST Echo</title></head><body>")
print("<h1>POST Echo</h1><hr/><ul>")
for k,v in params.items():
    safe = ", ".join(html.escape(x) for x in v)
    print(f"<li><b>{html.escape(k)}</b> = {safe}</li>")
print("</ul></body></html>")
