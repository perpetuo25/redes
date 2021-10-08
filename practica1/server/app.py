from flask import Flask, jsonify, request
from utils import suma_peticion
import psutil    

app = Flask(__name__)

@app.route("/", methods=["GET"])
def recibe():
    return jsonify({"variable": 0})

@app.route("/suma", methods= ["POST"])
def suma():
    resultado = suma_peticion(request)
    return jsonify(resultado)

@app.route("/finish", methods= ["GET"])
def resultado():
    return jsonify({"name": "compu1"})

@app.route("/getram", methods= ["GET"])
def ram():
    ram = psutil.virtual_memory().total / 1e+9
    return jsonify({"ram": ram})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
