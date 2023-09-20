from geopy import geocoders
from telebot import types


class GeoService:
    def __init__(self) -> None:
        self.geocoders = geocoders
        self.geolocator = geocoders.Nominatim(user_agent="jarvis_bot")

    def __get_location_from_message(self, message: types.Message):
        latitude = message.location.latitude
        longitude = message.location.longitude
        return self.geolocator.reverse((latitude, longitude), exactly_one=True)

    def get_geo_by_city(self, city: str) -> tuple[str, str]:
        latitude = str(self.geolocator.geocode(city).latitude)
        longitude = str(self.geolocator.geocode(city).longitude)
        return f"{latitude}, {longitude}"

    def get_city_by_message(self, message: types.Message) -> str:
        location = self.__get_location_from_message(message)
        print(location.raw.get("address", {}))
        city = location.raw.get("address", {}).get("city")

        if city:
            return f"Ваш город: {city}"
        else:
            return "Не удалось определить ваш город."

    def get_postal_code_by_message(self, message: types.Message) -> str:
        location = self.__get_location_from_message(message)
        postal_code = location.raw.get("address", {}).get("postcode")
        return postal_code
