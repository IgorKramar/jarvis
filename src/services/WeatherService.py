from src.config.index import ACCU_WEATHER_API_KEY

class WeatherService:
  def __init__(self) -> None:
    self.api_key = ACCU_WEATHER_API_KEY