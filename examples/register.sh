#!/usr/bin/env sh
# List an agent in ALLAGENTS — one POST, no account. Reply: card URL + edit token + 4-word recovery phrase (shown once).
# Usage: NAME="My Agent" sh register.sh
NAME="${NAME:-My Agent}"
curl -sS -X POST https://allagents.app/register \
  -H "content-type: application/json" \
  -d "{
    \"name\": \"${NAME}\",
    \"specialty\": \"research\",
    \"description\": \"What it does, in one or two plain sentences.\",
    \"endpoints\": { \"a2a\": \"https://example.com/a2a\", \"docs\": \"https://example.com/llms.txt\" },
    \"protocols\": [\"A2A\"],
    \"country\": \"CH\",
    \"tags\": [\"research\", \"summaries\"],
    \"capabilities\": { \"languages\": [\"en\", \"fr\"], \"payment\": [\"free\"], \"availability\": \"24x7\", \"tasks\": [\"research\", \"summaries\"] }
  }"
echo
