# Binance Futures Trading Bot

## Overview
A Python command-line application that connects to the Binance Futures Testnet and allows users to place Market and Limit orders.

## Features
- Connects to Binance Futures Testnet
- Market Orders
- Limit Orders
- Input Validation
- Logging
- Error Handling

## Technologies Used
- Python 3
- python-binance
- python-dotenv

## Installation

```bash
git clone <repository-url>
cd trading_bot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

## Run

```bash
python cli.py
```

## Project Structure

```
trading_bot/
│
├── bot/
├── logs/
├── tests/
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Author

Krish

## Acknowledgement

This project was developed with guidance and code assistance from ChatGPT.