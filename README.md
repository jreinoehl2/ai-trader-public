# AI Trader
Welcome to the repo behind my trading experiment where AI manages a real-money portfolio.

# The Concept
**Can powerful large language models like ChatGPT actually generate smart trading decisions using real-time data?**

## Each trading day:

- I provide it trading data on the stocks in its portfolio.  
- Strict stop-loss rules apply.  
- Every week I allow it to use deep research to reevaluate its account.

# Features of This Repo
- Live trading scripts — used to evaluate prices and update holdings daily  
- LLM-powered decision engine — ChatGPT picks the trades  
- Performance tracking — CSVs with daily PnL, total equity, and trade history  
- Visualization tools — Matplotlib graphs comparing ChatGPT vs. Index  
- Logs & trade data — auto-saved logs for transparency  

# Why This Matters
AI is being hyped across every industry, but can it really manage money without guidance?

This project is an attempt to find out — with transparency, data, and a real budget.

# Future Enhancements

The next evolution of AI Trader is full autonomy — transforming it from a semi-automated experiment into a fully self-sufficient trading system. Here’s what’s planned:

1. Real-Time Data Ingestion

- The system will automatically pull live market data using APIs (Alpaca, Polygon.io, or WebSocket-based feeds) instead of relying on manual CSV uploads.

- It will continuously monitor price movements, technical indicators, and stop-loss conditions throughout the day.

2. Autonomous Decision-Making

- Using the live data stream, the AI engine will independently decide when to buy, sell, or hold — applying portfolio optimization and risk management logic without human intervention.

- Human input will shift from “manual trader” to “observer.”

3. Automated Trade Execution

- Integration with a real brokerage API (like Alpaca or Interactive Brokers) will allow the system to place live trades automatically.

- Stop-losses, take-profits, and order types (MOO, limit, trailing stop) will all be handled programmatically.

4. User Notifications & Transparency

- Every major decision — from trade execution to portfolio rebalancing — will trigger an instant notification via email or Microsoft Teams message.

- This ensures full visibility into the AI’s actions and reasoning, keeping the user (me) informed in real time.

5. Continuous Learning & Evaluation

- Future iterations may leverage reinforcement learning or fine-tuned LLM feedback loops to improve strategy adaptively based on performance metrics.

# Tech Stack & Features

## Core Technologies
- **Python** - Core scripting and automation
- **pandas + yFinance** - Market data fetching and analysis
- **Matplotlib** - Performance visualization and charting
- **ChatGPT-4** - AI-powered trading decision engine

## Key Features
- **Robust Data Sources** - Yahoo Finance primary, Stooq fallback for reliability
- **Automated Stop-Loss** - Automatic position management with configurable stop-losses
- **Interactive Trading** - Market-on-Open (MOO) and limit order support
- **Backtesting Support** - ASOF_DATE override for historical analysis
- **Performance Analytics** - CAPM analysis, Sharpe/Sortino ratios, drawdown metrics
- **Trade Logging** - Complete transparency with detailed execution logs

## System Requirements
- Python  3.11+
- Internet connection for market data
- ~10MB storage for CSV data files
