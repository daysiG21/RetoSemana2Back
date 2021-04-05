from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
tareas=[]

@app.route("/")
def inicio():
  return "Lista de tareas"

@app.route("/tareas", methods=["GET","POST"])
def manejo_tareas():
  if request.method=="GET":
    if tareas:
      return{
        "ok":True,
        "content":tareas,
        "message":None
      }
    else:
      return{
        "ok":False,
        "content":None,
        "message":"No hay tareas"
      },404
  elif request.method=="POST": 
    data = request.get_json()
    tareas.append(data)
    return{
      "ok":True,
      "content":None,
      "message":"Tarea Registrada"
    },201

@app.route("/tarea/<int:id>", methods=["PUT","DELETE"])
def tarea(id):
  if len(tareas)>id:
    if request.method=="PUT":
      data = request.get_json()
      tareas[id]=data
      return {
        "ok":True,
        "content":tareas[id],
        "message":"Tarea actualizada"
      },201
    elif request.method=="DELETE":
      tarea = tareas.pop(id)
      return {
        "ok":True,
        "content":tarea,
        "message":"Tarea eliminada"
      },200

app.run(debug=True, port="3000")