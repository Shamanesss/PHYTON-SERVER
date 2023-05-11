import sqlite3
con=sqlite3.content("WEATHER.db")
cur=con.cursor()
cur.execute ("CREATE TABLE cities(id,name,temperature,rain_probability)")



def create (weather):
    WEATHER_DATA[weather['id']]=weather

def read (weather):
    return WEATHER_DATA.get(id)

def read ():
    res = cur.execute("SELECT name FROM cities")
    resultado = res.fetchone
    print(resultado)
    return resultado


def delete (id):
    del WEATHER_DATA [id]