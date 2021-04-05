from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
departamento=["Amazonas","Áncash","Apurímac","Arequipa"
,"Ayacucho","Cajamarca","Callao","Cusco","Huancavelica"
,"Huánuco","Ica","Junín","La Libertad","Lambayeque"
,"Lima","Loreto","Madre de Dios","Moquegua","Pasco"
,"Piura","Puno","San Martín","Tacna","Tumbes","Ucayali"]

@app.route("/")
def inicio():
  return "Servidor Existoso"

@app.route("/departamentos", methods=["GET"])
def lista_dep():
  if request.method=="GET":
    if departamento:
      return {
        "ok":True,
        "content":departamento,
        "message":"Lista de departamentos"
      }
    else:
      return{
        "ok":False,
        "content":None,
        "message":"No hay departamentos"
      },404
app.run(debug=True, port=5000) 
