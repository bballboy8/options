# ActivFinancial Samples

A collection of Python samples demonstrating the usage of ActivFinancial's API for market data streaming and analysis.

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

3. Install the ActivFinancial package:
```bash
pip install activfinancial-1.11.0-py3-none-win_amd64.whl
```

4. Install other dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your API credentials and preferences.

## Configuration

The following environment variables can be configured in the `.env` file:

- `ACTIV_API_KEY`: Your ActivFinancial API key
- `ACTIV_WS_URL`: WebSocket URL for the API
- `SYMBOLS`: Comma-separated list of symbols to track
- `SAVE_INTERVAL`: Number of trades before saving to CSV (default: 100)

## Available Samples

### Stock Trade Stream (`activ_sample.py`)
A Python application that streams live stock trades from ActivFinancial API, measures latency, and stores the data in a CSV file.

Run the sample:
```bash
python activ_sample.py
```

The script will:
1. Connect to the ActivFinancial WebSocket API
2. Subscribe to live trade data for the configured symbols
3. Process trades and calculate latency
4. Save data to `stock_trades.csv` at the configured interval

### Test Sample (`sample_test.py`)
A test script demonstrating basic ActivFinancial API functionality.

Run the test:
```bash
python sample_test.py
```

## Output

The trade stream generates a CSV file (`stock_trades.csv`) with the following columns:
- symbol: Stock symbol
- price: Trade price
- size: Trade size
- timestamp: Trade timestamp
- latency_ms: Latency in milliseconds

## Dependencies

- activfinancial==1.11.0
- pandas>=2.2.3
- websockets>=15.0.1
- requests>=2.32.3
- python-dotenv>=1.0.0

## Logging

The scripts log important events and errors to the console, including:
- Connection status
- Subscription confirmations
- Trade processing statistics
- Error messages 