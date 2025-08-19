import os, json, secrets, time

SESS_DIR = "/tmp/py_sessions"
COOKIE_NAME = "CGISESSID"

def load_session(environ, headers):
    # Get session id (sid) from Cookie
    cookies = environ.get("HTTP_COOKIE", "")
    sid = None
    for part in cookies.split(";"):
        part = part.strip()
        if not part:
            continue
        k, _, v = part.partition("=")
        if k == COOKIE_NAME:
            sid = v or None
            break

    # If no sid, generate a new one and add Set-Cookie header
    if not sid:
        sid = secrets.token_hex(16)
        headers.append(f"Set-Cookie: {COOKIE_NAME}={sid}; Path=/; HttpOnly")

    # Read existing session file or start empty session
    path = os.path.join(SESS_DIR, f"{sid}.json")
    data = {}
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except Exception:
            data = {}
    return sid, data, path

def save_session(path, data):
    # Ensure session directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Save session data to file
    with open(path, "w") as f:
        json.dump(data, f)
