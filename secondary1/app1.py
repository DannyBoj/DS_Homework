import time
import requests
from flask import Flask, request

app = Flask(__name__)

message_dict = {}
n = 0

@app.route('/api', methods=['POST'])
def write():
    msg = request.get_json()
    global n
    message_dict[n] = msg
    n += 1
    time.sleep(5)
    return 'Response successful', 200

@app.route('/api', methods=['GET'])
def get_message():
    return message_dict, 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 6000)
