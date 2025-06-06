import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

PORT = int(os.getenv('PORT', '8080'))
BIN_CHANNEL = int(os.getenv("BIN_CHANNEL"))
STREAM_URL = os.getenv("URL")
