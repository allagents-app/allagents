# Agent escrow (ERC-8183) on Base: who evaluates the work?

*30 days to 29 October 2026 — blocks 51,950,445 to 53,244,162*

ERC-8183 ("Agentic Commerce", a draft standard since 25 February 2026) lets an AI agent pay another agent into an escrow contract; an evaluator then marks the job complete, which pays the provider, or rejects it, which refunds the client. We read the public events of its largest deployment on Base, the ACP v2 contract `0x238E541BfefD82238730D00a2208E5497F1832E0`, over 30 days:

| Jobs | Count |
|---|---|
| Created | 1,171 |
| Funded | 1,013 |
| Submitted | 985 |
| Completed | 929 |
| Rejected | 22 |
| Expired | 77 |
| Refunded | 81 |

- **Who evaluates:** in 1,152 of the 1,171 jobs (98.4 %), the evaluator was the client itself.
- **Money in escrow:** 282 fundings had a non-zero amount, 134.86 USDC in total; median 0.02 USDC, largest 20 USDC.
- **Clients:** 59 distinct; one wallet (`0x22cb…ae40`) created 627 jobs (53.5 %).

Method: `eth_getLogs` on the contract through public Base nodes; job creation identified by the standard's `JobCreated(uint256,address,address,address,uint256,address)` event; amounts cross-checked with USDC transfers into the contract (134.86 USDC in).
