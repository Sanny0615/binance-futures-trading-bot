import os

from dotenv import load_dotenv
from binance.client import Client

# Load environment variables from .env
load_dotenv()

# Read API credentials
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Validate credentials
if not API_KEY or not SECRET_KEY:
    raise ValueError(
        "API_KEY and SECRET_KEY not found. Please check your .env file."
    )

# Create Binance Testnet client
client = Client(
    api_key=API_KEY,
    api_secret=SECRET_KEY,
    testnet=True
)


def test_connection():
    """
    Test the Binance API connection.
    """
    try:
        account = client.futures_account()

        print("✅ Connected to Binance Futures Testnet")
        print(f"Account Alias: {account.get('alias', 'N/A')}")

        return True

    except Exception as e:
        print("❌ Connection Failed")
        print(e)
        return False


if __name__ == "__main__":
    test_connection()