from flask import Flask, render_template, jsonify, request
import uuid
import random
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['POST'])
def generate_key():
    key_count = request.json.get('keyCount', 1)
    keys = [generate_key_process() for _ in range(key_count)]
    return jsonify(keys)

def login(client_id):
    time.sleep(random.uniform(1, 3))
    return str(uuid.uuid4())

def generate_key_process():
    client_id = str(uuid.uuid4())
    client_token = login(client_id)
    time.sleep(random.uniform(1, 3))
    return str(uuid.uuid4())


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
