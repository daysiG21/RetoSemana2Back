from flask import Flask, request

from flask_cors import CORS

app = Flask(__name__)

CORS(app)
colores=[]

@app.route("/")
def inicio():
  return "Servidor para el ingreso de colores"

@app.route("/color", methods=['POST'])
def manejo_colores():
  if request.method=="POST":
    data=request.get_json()
    colores.append(data)
    return{
      "ok":True,
      "content":None,
      "message":"Color agregado correctamente"
    },201

@app.route("/colores",methods=["GET"])
def lista_colores():
  if request.method=="GET":
    if colores:
      return{
        "ok":True,
        "content":colores,
        "message":None
      }
    else:
      return{
        "ok":False,
        "content":None,
        "message":"No hay colores registrados"
      },404

app.run(debug=True, port=4000)
