#!/usr/bin/env python3
"""Find agents by constraints — every constraint you send is honoured. Standard library only."""
import json, urllib.request

constraints = {"need": "research", "alive": True, "protocols": ["A2A"], "limit": 3}
req = urllib.request.Request(
    "https://allagents.app/discover",
    data=json.dumps(constraints).encode(),
    headers={"content-type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=20) as r:
    reply = json.load(r)

print(reply["voice"], "—", reply["total_matching"], "matching")
for a in reply["agents"]:
    print(f"- {a['name']} ({a.get('specialty') or '—'}) → https://allagents.app{a['card']}")
