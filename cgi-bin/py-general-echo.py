#!/usr/bin/env python3
import os, sys, html
print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=UTF-8\n")
method = os.environ.get("REQUEST_METHOD","")
qs = os.environ.get("QUERY_STRING","")
length = int(os.environ.get("CONTENT_LENGTH","0") or 0)
body = sys.stdin.read(length) if length>0 else ""
print("<!doctype html><html><head><title>Python General Echo</title></head><body>")
print("<h1>General Request Echo</h1><hr/>")
print(f"<p><b>Method:</b> {html.escape(method)}</p>")
print(f"<p><b>Query String:</b> {html.escape(qs)}</p>")
print("<p><b>Body:</b></p><pre>")
print(html.escape(body))
print("</pre></body></html>")
