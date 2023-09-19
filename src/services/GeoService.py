from geopy import geocoders

class GeoService:
  def __init__(self) -> None:
    self.geocoders = geocoders

  def get_geo_by_city(self, city: str) -> tuple[str, str]:
    geolocator = self.geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return f"{latitude}, {longitude}"