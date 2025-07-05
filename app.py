from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({"message": "Personalized Plan API is running!"})

@app.route("/plan", methods=["POST"])
def generate_plan():
    try:
        data = request.get_json()

        diabetes_type = data.get("diabetes_type", "").capitalize()
        diagnosis_date = data.get("diagnosis_date", "")
        a1c_value = float(data.get("a1c_value", 0))
        activity_level = data.get("activity_level", "").capitalize()
        goals = data.get("goals", "")
        email = data.get("email", "Not provided")

        # Custom logic for A1c interpretation
        if a1c_value < 5.7:
            a1c_status = "Excellent control. Keep maintaining your healthy lifestyle."
        elif 5.7 <= a1c_value < 6.5:
            a1c_status = "You’re in the prediabetic range. Lifestyle changes now can prevent complications."
        elif 6.5 <= a1c_value < 8.0:
            a1c_status = "A1c is in the moderate range. Consider dietary adjustments and increased activity."
        else:
            a1c_status = "High A1c. Consult your doctor. Medication or intensive changes may be needed."

        # Suggestions based on activity level
        if activity_level.lower() == "low":
            activity_suggestion = "Start with 10-minute walks after meals. Gradually build up to 30 minutes/day."
        elif activity_level.lower() == "moderate":
            activity_suggestion = "Maintain your current activity. Consider adding light strength training."
        else:
            activity_suggestion = "You have an active lifestyle—great job! Keep tracking your progress."

        # Final HTML block
        plan_html = f"""
        <div style='font-family:Arial, sans-serif; line-height:1.6;'>
            <h3 style='color:#2e6d5c;'>Your Personalized Diabetes Management Plan</h3>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Diabetes Type:</strong> {diabetes_type}</p>
            <p><strong>Diagnosis Date:</strong> {diagnosis_date}</p>
            <p><strong>Latest A1c:</strong> {a1c_value}%</p>
            <p><strong>A1c Insight:</strong> {a1c_status}</p>
            <p><strong>Activity Level:</strong> {activity_level}</p>
            <p><strong>Suggestion:</strong> {activity_suggestion}</p>
            <p><strong>Your Wellness Goals:</strong> {goals}</p>

            <div style='background:#fff3cd; border:1px solid #ffeeba; color:#856404; padding:1rem; margin-top:2rem; border-radius:8px;'>
                <strong>Disclaimer:</strong> This AI-generated plan is for informational use only. It is intended for women and should not replace professional medical advice. Always consult your doctor before making health decisions.
            </div>
        </div>
        """

        return jsonify({"plan_html": plan_html})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
