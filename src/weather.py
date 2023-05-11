from .weather_repository_sqlite import *


def get_weather_by(id):
    return read (id)

def list_weather_all():
    return read ()

def add_city(weather):
    rain_probality=0.7
    weather["rain_probality"]=rain_probality
    create (weather)

def delete_cities(id):
     delete(id)