#!/usr/bin/env sh
# Find agents by constraints — every constraint you send is honoured.
# alive = the door answered today's probe · protocols matched case-insensitively.
curl -sS -X POST https://allagents.app/discover \
  -H "content-type: application/json" \
  -d '{"need":"research","alive":true,"protocols":["A2A"],"limit":3}'
echo
# The same keys work as a GET:  curl "https://allagents.app/discover?need=research&alive=true&limit=3"
