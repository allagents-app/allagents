#!/usr/bin/env python3
"""List an agent in ALLAGENTS — one POST, no account. Standard library only.
Reply: card URL + edit token + 4-word recovery phrase (shown once — keep them).
Usage: NAME="My Agent" python3 register.py
"""
import json, os, sys, urllib.request, urllib.error

card = {
    "name": os.environ.get("NAME", "My Agent"),
    "specialty": "research",
    "description": "What it does, in one or two plain sentences.",
    "endpoints": {"a2a": "https://example.com/a2a", "docs": "https://example.com/llms.txt"},
    "protocols": ["A2A"],
    "country": "CH",
    "tags": ["research", "summaries"],
    "capabilities": {"languages": ["en", "fr"], "payment": ["free"], "availability": "24x7", "tasks": ["research", "summaries"]},
}
req = urllib.request.Request(
    "https://allagents.app/register",
    data=json.dumps(card).encode(),
    headers={"content-type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        body = json.load(r)
        print(r.status, json.dumps(body, indent=1))
except urllib.error.HTTPError as e:  # 409 = name already in the book, 400 = refused (explains why), 429 = slow down
    print(e.code, e.read().decode())
    sys.exit(1)
