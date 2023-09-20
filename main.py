from src.config.index import TG_BOT_API_KEY
from src.main.Bot import Bot

if __name__ == "__main__":
    tg_bot = Bot(TG_BOT_API_KEY)
    tg_bot.start()
