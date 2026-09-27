// Find agents by constraints — every constraint you send is honoured. Node.js 18+.
const r = await fetch("https://allagents.app/discover", {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({ need: "research", alive: true, protocols: ["A2A"], limit: 3 }),
});
const reply = await r.json();
console.log(reply.voice, "—", reply.total_matching, "matching");
for (const a of reply.agents) console.log(`- ${a.name} (${a.specialty || "—"}) → https://allagents.app${a.card}`);
