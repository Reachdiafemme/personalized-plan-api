from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_plan():
    data = request.get_json()
    
    plan = []

    if float(data.get('a1c_value', 0)) > 7.5:
        plan.append("🌿 Reduce A1c with low-carb dinners and Cinnamon Herbal Tea.")
    if data.get('activity_level') == 'low':
        plan.append("🚶‍♀️ Start daily 15-minute walks after meals.")
    if "energy" in data.get('goals', '').lower():
        plan.append("🧘 Try deep sleep + hydration tracking.")

    plan.append("✅ Log daily values in the Diafemme Wellness Tracker.")

    return jsonify({ "plan_html": "<p>" + "</p><p>".join(plan) + "</p>" })

if __name__ == '__main__':
    app.run()
