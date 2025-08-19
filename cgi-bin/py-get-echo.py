#!/usr/bin/env python3
import os, urllib.parse, html
print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=UTF-8\n")
qs = os.environ.get("QUERY_STRING","")
params = urllib.parse.parse_qs(qs, keep_blank_values=True)
print("<!doctype html><html><head><title>Python GET Echo</title></head><body>")
print("<h1>GET Echo</h1><hr/><ul>")
for k,v in params.items():
    safe = ", ".join(html.escape(x) for x in v)
    print(f"<li><b>{html.escape(k)}</b> = {safe}</li>")
print("</ul></body></html>")
