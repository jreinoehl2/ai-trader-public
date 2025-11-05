# AI Trader API

Clean, minimal FastAPI service that lets an AI (or a human script) place paper trades through Alpaca with guardrails for risk management.

## 1. Overview
The project exposes a small, opinionated trading API. It focuses on safety (whitelisted symbols, per‑order dollar caps, market‑open checks) rather than strategy. You can layer an AI decision engine on top without giving it unlimited power.

## 2. Core Concept
Can an AI make sensible trading decisions if you give it a constrained, transparent interface? This API is that interface: it accepts structured or simple natural language trade commands and enforces limits before forwarding to Alpaca's paper trading endpoint.

## 3. Features
| Category | Highlights |
|----------|-----------|
| Order Safety | Symbol whitelist, max dollar value per order, cash balance & market‑open validation |
| Command Parsing | Natural language shortcut (e.g. `buy NVDA --2`) mapped to structured order model |
| Paper Trading | All activity confined to Alpaca paper account |
| Health & Status | Account, positions, health endpoint for deployment checks |
| Deployment Ready | Docker + `render.yaml` for Render.com hosting |

## 4. Architecture
```
root
├─ render.yaml              # Render.com service definition
├─ server/
│  ├─ requirements.txt      # Python dependencies (FastAPI, Alpaca helpers etc.)
│  └─ app/
│     ├─ main.py            # FastAPI app factory & middleware
│     ├─ api.py             # Route handlers & validation helpers
│     ├─ alpaca.py          # Thin wrapper around Alpaca REST API
│     ├─ config.py          # Environment variable loading & constants
│     └─ Dockerfile         # Container image build instructions
├─ bot/                     # (Placeholder for future AI decision agent)
├─ widget/                  # (Placeholder for future dashboard/UI)
└─ README.md
```

### Key Modules
- `main.py` sets up the FastAPI app with CORS.
- `api.py` contains endpoint handlers plus internal guard functions.
- `alpaca.py` abstracts Alpaca REST calls (account, quotes, orders).
- `config.py` reads environment variables (e.g. `ALLOWED_SYMBOLS`, `MAX_ORDER_VALUE`).

## 5. API Endpoints (Planned / Implemented)
| Method | Path | Purpose |
|--------|------|---------|
| POST | `/buy-text` | Accept natural language order string (e.g. `buy AAPL --1`). |
| POST | `/order` | Place structured order `{ symbol, qty, side }`. |
| GET  | `/account` | Retrieve paper account balances & status. |
| GET  | `/positions` | List open positions. |
| GET  | `/healthz` | Simple health check for Render.

## 6. Data & Validation Flow
1. Incoming request (text or JSON).
2. Parse into `OrderRequest` (Pydantic model).
3. Guards run:
   - Symbol is uppercased & checked against whitelist.
   - Market open verified from Alpaca clock.
   - Latest quote retrieved; estimated cost computed.
   - Cash & per‑order cap enforced.
4. Order forwarded to Alpaca paper endpoint (not shown in README code but handled in `alpaca.py`).

## 7. Environment Variables
| Name | Description | Example |
|------|-------------|---------|
| `ALPACA_API_KEY` | Alpaca paper trading API key | `PKxxxxxxxx` |
| `ALPACA_API_SECRET` | Alpaca paper trading secret | `SKxxxxxxxx` |
| `ALLOWED_SYMBOLS` | Comma list of tradable tickers | `AAPL,MSFT,NVDA,SPY` |
| `MAX_ORDER_VALUE` | Max dollar value per single order | `3000` |

Add a `.env` file (based on `server/.env.example`) or configure via Render dashboard. Never commit real keys.

## 8. Installation
```bash
git clone https://github.com/jreinoehl2/ai-trader-public.git
cd ai-trader-public
python -m venv .venv
.venv\Scripts\activate                # Windows
pip install -r server/requirements.txt
cp server/.env.example server/.env     # then edit values
```

## 9. Running Locally
```bash
cd server/app
uvicorn main:app --reload
# Visit http://localhost:8000
```

## 10. Example Usage
```bash
curl -X POST http://localhost:8000/buy-text \
  -H "Content-Type: application/json" \
  -d '{"command":"buy NVDA --2"}'

curl http://localhost:8000/account
curl http://localhost:8000/positions
```

## 11. Safety & Limitations
- Paper trading only (no real capital risk by default).
- Whitelist & dollar caps prevent over‑exposure.
- No strategy logic included – this layer is intentionally thin.
- External AI agent integration left to user (e.g. call endpoints from a separate process).

## 12. Roadmap
- Implement remaining endpoints in `api.py` (account, positions if not complete).
- Add rate limiting & audit logging.
- Introduce AI agent module in `bot/` for autonomous decision cycles.
- Add test suite (Pytest) & CI workflow.
- Basic front‑end dashboard in `widget/`.

## 13. Contributing
Open an issue or fork & PR. Please include:
- Clear description of the change.
- Tests covering new behavior (once test framework added).

## 14. License
Add a license file (MIT recommended) – currently unspecified.
