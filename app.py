
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Diafemme Personalized Plan API is running."

@app.route('/plan', methods=['POST'])
def generate_plan():
    data = request.get_json()

    email = data.get("email", "Not provided")
    diabetes_type = data.get("diabetes_type", "Not specified")
    diagnosis_date = data.get("diagnosis_date", "Not specified")
    a1c_value = data.get("a1c_value", "Not specified")
    activity_level = data.get("activity_level", "Not specified")
    goals = data.get("goals", "Not specified")

    plan_html = f"""
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Diabetes Type:</strong> {diabetes_type}</p>
    <p><strong>Diagnosis Date:</strong> {diagnosis_date}</p>
    <p><strong>Latest A1c (%):</strong> {a1c_value}</p>
    <p><strong>Activity Level:</strong> {activity_level}</p>
    <p><strong>Wellness Goals:</strong> {goals}</p>
    <p>This is a basic preview. A tailored plan is being developed.</p>
    """

    return jsonify({
        "status": "success",
        "plan_html": plan_html
    })

if __name__ == '__main__':
    app.run(debug=True)
