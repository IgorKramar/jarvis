import telebot
from telebot import types

from src.services.WeatherService import WeatherService
from src.services.GeoService import GeoService

from src.constants.user_states import USER_STATES


class Bot:
    def __init__(self, api_key):
        self.bot = telebot.TeleBot(api_key)
        self.weatherService = WeatherService()
        self.geoService = GeoService()
        self.user_states = {}

    # === SYSTEM ===

    def start(self):
        self.register_command_handlers()
        self.run_bot()

    def run_bot(self):
        self.bot.infinity_polling()

    # === REGISTER COMMANDS ===

    def register_command_handlers(self):
        @self.bot.message_handler(commands=["start", "help"])
        def _(message):
            self.send_welcome(message)

        @self.bot.message_handler(commands=["weather"])
        def _(message):
            self.get_weather(message)

        @self.bot.message_handler(func=lambda message: True)
        def _(message):
            self.echo_message(message)

        @self.bot.message_handler(
            func=lambda message: self.user_states.get(message.chat.id)
            == USER_STATES.WAITING_FOR_LOCATION,
            content_types=["location"],
        )
        def _(message):
            self.get_weather_location(message)

    # === HANDLERS ===

    def send_welcome(self, message):
        self.bot.reply_to(message, "Howdy, how are you doing?")

    def echo_message(self, message):
        self.bot.reply_to(message, message.text)

    def get_weather(self, message):
        self.user_states[message.chat.id] = USER_STATES.WAITING_FOR_LOCATION
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item = types.KeyboardButton("Отправить местоположение", request_location=True)
        markup.add(item)

        self.bot.send_message(
            message.chat.id,
            "Пожалуйста, отправьте ваше текущее местоположение:",
            reply_markup=markup,
        )

    def get_weather_location(self, message):
        city_message = self.geoService.get_city_by_message(message)
        markup = types.ReplyKeyboardRemove()
        self.bot.send_message(message.chat.id, city_message, reply_markup=markup)
        self.user_states[message.chat.id] = None
