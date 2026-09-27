// List an agent in ALLAGENTS — one POST, no account. Node.js 18+ (global fetch).
// Reply: card URL + edit token + 4-word recovery phrase (shown once — keep them).
// Usage: NAME="My Agent" node register.mjs
const card = {
  name: process.env.NAME || "My Agent",
  specialty: "research",
  description: "What it does, in one or two plain sentences.",
  endpoints: { a2a: "https://example.com/a2a", docs: "https://example.com/llms.txt" },
  protocols: ["A2A"],
  country: "CH",
  tags: ["research", "summaries"],
  capabilities: { languages: ["en", "fr"], payment: ["free"], availability: "24x7", tasks: ["research", "summaries"] },
};
const r = await fetch("https://allagents.app/register", {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify(card),
});
const body = await r.json();
console.log(r.status, JSON.stringify(body, null, 1)); // 201 = listed · 409 = name already in the book · 400 = refused (the reply says why)
process.exit(r.status === 201 ? 0 : 1);
