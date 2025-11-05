# AI Trader API# AI Trader API



A FastAPI-based trading API that enables AI-driven trading decisions through integration with Alpaca's paper trading platform.A FastAPI-based trading API that enables AI-driven trading decisions through integration with Alpaca's paper trading platform.



## The Concept## The Concept



**Can AI make intelligent trading decisions through a simple, constrained API?****Can AI make intelligent trading decisions through a simple, constrained API?**



This project provides a RESTful API that:This project provides a RESTful API that:

- Accepts natural language trading commands (e.g., "buy NVDA --2")- Accepts natural language trading commands (e.g., "buy NVDA --2")

- Validates trades against safety rules and market conditions- Validates trades against safety rules and market conditions

- Executes orders through Alpaca's paper trading API- Executes orders through Alpaca's paper trading API

- Enforces symbol whitelists and order value caps for risk management- Enforces symbol whitelists and order value caps for risk management



## Architecture# Features of This Repo

- Live trading scripts — used to evaluate prices and update holdings daily  

### API Server (`/server`)- LLM-powered decision engine — ChatGPT picks the trades  

- **FastAPI** web framework with CORS support- Performance tracking — CSVs with daily PnL, total equity, and trade history  

- **Alpaca integration** for market data and order execution- Visualization tools — Matplotlib graphs comparing ChatGPT vs. Index  

- **Trade validation** with configurable safety guards- Logs & trade data — auto-saved logs for transparency  

- **Docker deployment** ready for Render.com

# Why This Matters

### Key ComponentsAI is being hyped across every industry, but can it really manage money without guidance?

- `api.py` - REST endpoints for trading operations

- `alpaca.py` - Alpaca API client wrapperThis project is an attempt to find out — with transparency, data, and a real budget.

- `config.py` - Environment-based configuration

- `main.py` - FastAPI application entry point# Future Enhancements



## FeaturesThe next evolution of AI Trader is full autonomy — transforming it from a semi-automated experiment into a fully self-sufficient trading system. Here’s what’s planned:



### Trading Controls1. Real-Time Data Ingestion

- **Symbol Whitelist** - Only approved stocks can be traded (AAPL, MSFT, NVDA, SPY)

- **Order Value Caps** - Maximum $3,000 per order to limit risk- The system will automatically pull live market data using APIs (Alpaca, Polygon.io, or WebSocket-based feeds) instead of relying on manual CSV uploads.

- **Market Hours Validation** - Prevents trading when market is closed

- **Cash Balance Checks** - Ensures sufficient funds before placing orders- It will continuously monitor price movements, technical indicators, and stop-loss conditions throughout the day.



### API Endpoints2. Autonomous Decision-Making

- `POST /buy-text` - Natural language trade commands

- `POST /order` - Direct order placement- Using the live data stream, the AI engine will independently decide when to buy, sell, or hold — applying portfolio optimization and risk management logic without human intervention.

- `GET /account` - Account balance and positions

- `GET /positions` - Current holdings- Human input will shift from “manual trader” to “observer.”

- `GET /healthz` - Health check for monitoring

3. Automated Trade Execution

## Tech Stack

- Integration with a real brokerage API (like Alpaca or Interactive Brokers) will allow the system to place live trades automatically.

- **FastAPI** - Modern Python web framework

- **Uvicorn** - ASGI server- Stop-losses, take-profits, and order types (MOO, limit, trailing stop) will all be handled programmatically.

- **Pydantic** - Data validation

- **Alpaca API** - Paper trading platform4. User Notifications & Transparency

- **Docker** - Containerized deployment

- **Render.com** - Cloud hosting platform- Every major decision — from trade execution to portfolio rebalancing — will trigger an instant notification via email or Microsoft Teams message.



## Setup- This ensures full visibility into the AI’s actions and reasoning, keeping the user (me) informed in real time.



### Prerequisites5. Continuous Learning & Evaluation

- Python 3.11+

- Alpaca paper trading account- Future iterations may leverage reinforcement learning or fine-tuned LLM feedback loops to improve strategy adaptively based on performance metrics.

- API keys from Alpaca

# Tech Stack & Features

### Installation

## Core Technologies

1. Clone the repository:- **Python** - Core scripting and automation

```bash- **pandas + yFinance** - Market data fetching and analysis

git clone https://github.com/jreinoehl2/ai-trader-public.git- **Matplotlib** - Performance visualization and charting

cd ai-trader-public- **ChatGPT-4** - AI-powered trading decision engine

```

## Key Features

2. Create a virtual environment:- **Robust Data Sources** - Yahoo Finance primary, Stooq fallback for reliability

```bash- **Automated Stop-Loss** - Automatic position management with configurable stop-losses

python -m venv .venv- **Interactive Trading** - Market-on-Open (MOO) and limit order support

.venv\Scripts\activate  # Windows- **Backtesting Support** - ASOF_DATE override for historical analysis

# or- **Performance Analytics** - CAPM analysis, Sharpe/Sortino ratios, drawdown metrics

source .venv/bin/activate  # macOS/Linux- **Trade Logging** - Complete transparency with detailed execution logs

```

## System Requirements

3. Install dependencies:- Python  3.11+

```bash- Internet connection for market data

pip install -r server/requirements.txt- ~10MB storage for CSV data files

```

4. Configure environment variables:
```bash
cp server/.env.example server/.env
# Edit server/.env with your Alpaca API credentials
```

5. Run the development server:
```bash
cd server/app
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Configuration

Environment variables (set in `.env` or deployment platform):

- `ALPACA_API_KEY` - Your Alpaca API key
- `ALPACA_API_SECRET` - Your Alpaca secret key
- `ALLOWED_SYMBOLS` - Comma-separated list of tradeable symbols (default: AAPL,MSFT,NVDA,SPY)
- `MAX_ORDER_VALUE` - Maximum dollar value per order (default: 3000)

## Deployment

This project is configured for deployment on Render.com using Docker.

1. Push to GitHub
2. Connect repository to Render
3. Configure environment variables in Render dashboard
4. Deploy using `render.yaml` configuration

## API Usage Examples

### Place a trade using natural language:
```bash
curl -X POST "http://localhost:8000/buy-text" \
  -H "Content-Type: application/json" \
  -d '{"command": "buy NVDA --2"}'
```

### Check account status:
```bash
curl "http://localhost:8000/account"
```

### View current positions:
```bash
curl "http://localhost:8000/positions"
```

## Safety Features

- **Paper Trading Only** - All trades execute on Alpaca's paper trading platform
- **Pre-trade Validation** - Symbols, cash, and market hours checked before execution
- **Order Limits** - Per-order caps prevent excessive risk
- **Restricted Symbols** - Only whitelisted stocks can be traded

## Future Enhancements

- **AI Agent Integration** - Connect LLM-based decision engine
- **Performance Analytics** - Track PnL, Sharpe ratio, drawdowns
- **Webhook Notifications** - Real-time alerts via email/Teams
- **Advanced Order Types** - Stop-loss, take-profit, trailing stops
- **Portfolio Optimization** - Automated rebalancing and risk management
- **Frontend Dashboard** - React-based UI for monitoring and control
