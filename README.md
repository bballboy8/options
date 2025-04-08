# Stock Trade Stream

A Python application that streams live stock trades from Options Technology API, measures latency, and stores the data in a CSV file.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your API credentials and preferences.

## Configuration

The following environment variables can be configured in the `.env` file:

- `OPTIONS_API_KEY`: Your Options Technology API key
- `OPTIONS_WS_URL`: WebSocket URL for the API (default: wss://api.options.com/stream)
- `SYMBOLS`: Comma-separated list of stock symbols to track (default: AAPL,MSFT,GOOGL)
- `SAVE_INTERVAL`: Number of trades before saving to CSV (default: 100)

## Usage

Run the script:
```bash
python stock_trade_stream.py
```

The script will:
1. Connect to the Options Technology WebSocket API
2. Subscribe to live trade data for the configured symbols
3. Process trades and calculate latency
4. Save data to `stock_trades.csv` at the configured interval

## Output

The script generates a CSV file (`stock_trades.csv`) with the following columns:
- symbol: Stock symbol
- price: Trade price
- size: Trade size
- timestamp: Trade timestamp
- latency_ms: Latency in milliseconds

## Logging

The script logs important events and errors to the console, including:
- Connection status
- Subscription confirmations
- Trade processing statistics
- Error messages 