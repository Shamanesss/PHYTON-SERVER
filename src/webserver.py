from flask import Flask,request
from .weather import *

app = Flask(__name__)

@app.route("/cities/<id>")
def cities(id):
    return get_weather_by(id)


@app.route("/cities")
def all_cities():
    return list_weather_all()

@app.route("/cities/",methods=["POST"])
def new_cities():
   # return add_city()
   data = request.get_json()
  
   print("*****new_city",data)
   add_city(data)
   return "ciudad agregada"


# @app.route("/cities/<id>",methods=["DELETE"])
# def delete_cities(id):
#    
#    del WEATHER_DATA [id]
#    return "ciudad borrada"

@app.route("/cities/<id>",methods=["DELETE"])
def kill_cities(id):
    delete_cities(id)
    return "ciudad borrada"

@app.route("/")
def hello_world():
    return "Hola Jone"

