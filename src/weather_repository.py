WEATHER_DATA={
  "BIO":{ "id": "BIO",
      "name": "Bilbao",
      "temperature": 11,
      "rain_probability": 0.9},
      

   "ROMA":{"id": "ROMA",
      "name": "Roma",
      "temperature": 25,
      "rain_probability": 0.3
    },

}

def create (weather):
    WEATHER_DATA[weather['id']]=weather

def read (weather):
    return WEATHER_DATA.get(id)

def read ():
    return WEATHER_DATA


def delete (id):
    del WEATHER_DATA [id]