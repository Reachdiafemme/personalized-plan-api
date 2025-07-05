
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Diafemme Personalized Plan API is Running."

@app.route("/plan", methods=["POST"])
def generate_plan():
    data = request.json

    # Extracting submitted data
    email = data.get("email", "user@example.com")
    diabetes_type = data.get("diabetes_type", "Not specified")
    diagnosis_date = data.get("diagnosis_date", "Unknown")
    a1c_value = data.get("a1c_value", "Not provided")
    activity_level = data.get("activity_level", "Unknown")
    goals = data.get("goals", "None")

    # Construct a simple HTML response
    plan_summary = f'''
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Diabetes Type:</strong> {diabetes_type}</p>
    <p><strong>Diagnosis Date:</strong> {diagnosis_date}</p>
    <p><strong>Latest A1c (%):</strong> {a1c_value}</p>
    <p><strong>Activity Level:</strong> {activity_level}</p>
    <p><strong>Goals:</strong> {goals}</p>
    <p>This is a sample personalized plan based on the information provided. For clinical advice, please consult a healthcare provider.</p>
    '''

    return jsonify({
        "plan_html": plan_summary,
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
