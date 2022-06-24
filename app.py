from email.mime import message
from flask import Flask, jsonify, request

app = Flask(__name__)

#Crear rutas
from intents import intents
from messages import messages

@app.route('/intents')
def getIntents():
    return jsonify({"intents": intents})

@app.route('/msg')
def getMsg():
    return jsonify({"messages": messages})

@app.route('/msg', methods=['POST'])
def addMsg():
    new_msg = {
        "id": request.json['id'],
        "msg": request.json['msg']
    }
    messages.append(new_msg)
    return jsonify({"message" : messages})

if __name__ == '__main__':
    app.run(debug=True, port=4000)