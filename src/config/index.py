import os
from dotenv import load_dotenv

load_dotenv()

TG_BOT_API_KEY = os.getenv('TG_BOT_API_KEY')
ACCU_WEATHER_API_KEY = os.getenv('ACCU_WEATHER_API_KEY')