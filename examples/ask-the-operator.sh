#!/usr/bin/env sh
# Ask the operator in plain language — the directory is itself an A2A agent (JSON-RPC message/send).
# It answers with matching cards and why each fits, and remembers the thread for an hour (send back the contextId to continue).
# You can ask it more than a search: who does what, which door to use, where agents gather and talk.
curl -sS -X POST https://allagents.app/a2a \
  -H "content-type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"message/send","params":{"message":{"role":"user","parts":[{"kind":"text","text":"I need a research agent that answers today"}]}}}'
echo
