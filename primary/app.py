import time
import requests
import json
from flask import Flask, request

app = Flask(__name__)

message_dict = {}
n = 0
def send_request(url, message):
    return requests.request(method = 'POST', url = url, json = message)

def call(message):
    r1, r2 = send_request('http://secondary1:6000/api', message), send_request('http://secondary2:7000/api', message)
    if r1.ok and r2.ok:
        return 'Messages were sent successfully', 200
    else:
        return 'Something went wrong', 400

@app.route('/api', methods=['POST'])
def write():
    msg = request.get_json()
    global n
    message_dict[n] = msg
    n+= 1
    result = call(msg)
    return result

@app.route('/api', methods=['GET'])
def get_message():
    return message_dict, 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
