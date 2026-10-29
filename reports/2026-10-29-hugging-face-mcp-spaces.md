# MCP servers on Hugging Face: how many are running?

*29 October 2026 — snapshot 12:30 UTC*

On 29 October 2026, Hugging Face listed **12,113 Spaces** that expose an MCP server. Reading their state through Hugging Face's public API, without calling any Space:

| State | Spaces |
|---|---|
| Running | 3,266 |
| Sleeping | 3,418 |
| Runtime error | 3,038 |
| Paused | 1,580 |
| Build error | 764 |
| Other | 47 |

Of the running Gradio Spaces with a description, the directory tested a first sample as MCP servers: about **88 %** answered (305 of 345). The most-liked ones are mostly image and video generation and editing.

Method: Hugging Face public API (`/api/spaces?filter=mcp-server`, runtime state), one MCP `initialize` call per tested running Space. Sleeping Spaces were not called.
