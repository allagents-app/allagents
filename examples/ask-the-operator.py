#!/usr/bin/env python3
"""Ask the operator in plain language — the directory is itself an A2A agent (JSON-RPC message/send).
Standard library only. Keep reply["result"]["contextId"] to continue the thread within the hour.
"""
import json, urllib.request

question = "I need a research agent that answers today"
rpc = {"jsonrpc": "2.0", "id": 1, "method": "message/send",
       "params": {"message": {"role": "user", "parts": [{"kind": "text", "text": question}]}}}
req = urllib.request.Request(
    "https://allagents.app/a2a",
    data=json.dumps(rpc).encode(),
    headers={"content-type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=30) as r:
    reply = json.load(r)

message = reply["result"]
print(message["parts"][0]["text"])
print("\ncontextId:", message.get("contextId"))
