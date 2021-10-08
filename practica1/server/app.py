from flask import Flask, jsonify, request
from utils import suma_peticion
from uuid import getnode as get_mac

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
    mac = get_mac()
    return jsonify({"Data": "PC de Eric ",
                    "Mac": str(mac)
    })

@app.route("/getram", methods= ["GET"])
def ram():
    ram = psutil.virtual_memory().total / 1e+9
    return jsonify({"ram": ram})
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
