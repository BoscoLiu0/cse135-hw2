#!/usr/bin/env python3
import os, json, datetime
print("Cache-Control: no-cache")
print("Content-Type: application/json; charset=UTF-8\n")
out = {
  "message": "Hello, Python (JSON)",
  "generated_at": datetime.datetime.utcnow().isoformat()+"Z",
  "ip": os.environ.get("REMOTE_ADDR","unknown")
}
print(json.dumps(out))
