#!/usr/bin/env python3
import os, datetime, sys
print("Cache-Control: no-cache")
print("Content-Type: text/html; charset=UTF-8\n")
ip = os.environ.get("REMOTE_ADDR","unknown")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")
print(f"""<!doctype html><html><head><title>Hello, Python!</title></head><body>
<h1>Hello, Python (HTML)</h1><hr/>
<p>Generated at: {now}</p>
<p>Your IP: {ip}</p>
</body></html>""")
