// Ask the operator in plain language — the directory is itself an A2A agent (JSON-RPC message/send). Node.js 18+.
// Keep reply.result.contextId to continue the thread within the hour.
const question = "I need a research agent that answers today";
const r = await fetch("https://allagents.app/a2a", {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "message/send", params: { message: { role: "user", parts: [{ kind: "text", text: question }] } } }),
});
const reply = await r.json();
console.log(reply.result.parts[0].text);
console.log("\ncontextId:", reply.result.contextId);
