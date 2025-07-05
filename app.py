from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Personalized Plan API is running!"})

@app.route('/plan', methods=['POST'])
def generate_plan():
    data = request.get_json()
    response = {
        "status": "success",
        "data_received": data
    }
    return jsonify(response)
