from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Personalized Plan API is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
