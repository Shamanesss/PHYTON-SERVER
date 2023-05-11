import sqlite3
con = sqlite3.content("WEATHER.db")
cur = con.cursor()
cur.execute("CREATE TABLE cities(id,name,temperature,rain_probability)")
con.commit()


def create(weather):
    cur.execute("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)",
                (weather['id'], weather['name'], weather['temperature'], weather['rain_probability']))
    con.commit()


def update(id, temperature, rain_probability):
    cur.execute("UPDATE cities SET temperature = ?, rain_probability = ? WHERE id = ?",
                (temperature, rain_probability, id))
    con.commit()


def read():
    res = cur.execute("SELECT name FROM cities")
    resultado = res.fetchone
    print(resultado)
    return resultado


def delete(id):
    cur.execute("DELETE FROM cities WHERE id = ?", (id,))
    con.commit()
