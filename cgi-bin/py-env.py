#!/usr/bin/env python3
import os, html
print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=UTF-8\n")
print("<!doctype html><html><head><title>Python Environment</title></head><body>")
print("<h1>Environment Variables</h1><hr/><pre>")
for k in sorted(os.environ):
    v = html.escape(os.environ[k])
    print(f"{k}={v}")
print("</pre></body></html>")
