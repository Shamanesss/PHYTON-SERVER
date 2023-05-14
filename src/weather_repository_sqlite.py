import sqlite3

con = sqlite3.connect("WEATHER.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS cities(
                id TEXT PRIMARY KEY,
                name TEXT,
                temperature NUMERIC,
                rain_probability real)""")

ciudades =[
    ("BAl","Bali", 18, 0.9),
    ("Can","canarias", 20, 0.3),
    
]

# def create(weather):
cur.executemany("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)", ciudades)
    # cur.execute("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)",
    #             (weather['id'], weather['name'], weather['temperature'], weather['rain_probability']))



# def update(id, temperature, rain_probability):
#     cur.execute("UPDATE cities SET temperature = ?, rain_probability = ? WHERE id = ?",
#                 (temperature, rain_probability, id))
#     con.commit()
cur.execute("UPDATE cities SET name='Austria' Where id='AUS'")

# def read():
cur.execute("SELECT * FROM cities")
ciudades = cur.fetchall()
for ciudad in ciudades:
    print(ciudad)

    # res= cur.execute("SELECT name FROM cities")
    # resultado = res.fetchone
    # print(resultado)
    # return resultado


# def delete(id):
#     cur.execute("DELETE FROM cities WHERE id = ?", (id,))
#     con.commit()

cur.execute("SELECT * FROM cities WHERE name = 'Bilbao'")
ciudades=cur.fetchall()
print(ciudades)


con.commit()
con.close()
