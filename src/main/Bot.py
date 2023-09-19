import telebot;

from src.services.WeatherService import WeatherService;
from src.services.GeoService import GeoService;

class Bot:
  def __init__(self, api_key):
    self.bot = telebot.TeleBot(api_key)
    self.weatherService = WeatherService()
    self.geoService = GeoService()

  # === SYSTEM ===

  def start(self):
    self.register_command_handlers()
    self.run_bot()

  def run_bot(self):
    self.bot.infinity_polling()

  # === REGISTER COMMANDS ===

  def register_command_handlers(self):
    @self.bot.message_handler(commands=['start', 'help'])
    def handle_start(message):
      self.send_welcome(message)

    @self.bot.message_handler(commands=['weather'])
    def handle_weather(message):
      self.get_weather(message)

    @self.bot.message_handler(func=lambda message: True)
    def handle_echo(message):
      self.echo_message(message)
  
  # === HANDLERS ===

  def send_welcome(self, message):
    self.bot.reply_to(message, "Howdy, how are you doing?")

  def echo_message(self, message):
    self.bot.reply_to(message, message.text)

  def get_weather(self, message):
    self.bot.reply_to(message, self.geoService.get_geo_by_city('Омск'))
