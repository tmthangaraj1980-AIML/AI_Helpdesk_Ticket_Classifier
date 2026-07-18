"""
=========================================================
AI Helpdesk Ticket Classifier
Flask Application Entry Point
=========================================================
"""

from flask import Flask, render_template, request, jsonify
import joblib
import os

# Import Helpdesk Data
from utils.helpdesk_data import HELPDESK_DATA

# -------------------------------------------------------
# Create Flask App
# -------------------------------------------------------

app = Flask(__name__)

# -------------------------------------------------------
# Load ML Model
# -------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "lr_model.pkl")
TFIDF_PATH = os.path.join(BASE_DIR, "models", "tfidf.pkl")

try:

    model = joblib.load(MODEL_PATH)
    tfidf = joblib.load(TFIDF_PATH)

    print("✅ Machine Learning model loaded successfully.")

except Exception as e:

    print("❌ Error loading model:", e)

    model = None
    tfidf = None


# -------------------------------------------------------
# Home Route
# -------------------------------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -------------------------------------------------------
# Prediction Route
# -------------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        ticket = data.get("ticket", "").strip()

        if ticket == "":

            return jsonify({

                "error": "Ticket cannot be empty."

            }), 400

        # TF-IDF Vectorization
        ticket_vector = tfidf.transform([ticket])

        # Prediction
        prediction = model.predict(ticket_vector)[0]

        # Probabilities
        probabilities = model.predict_proba(ticket_vector)[0]

        # Confidence
        confidence = round(float(max(probabilities) * 100), 2)

        # Top 3 Predictions
        top_indices = probabilities.argsort()[-3:][::-1]

        top_predictions = []

        for index in top_indices:

            top_predictions.append({

                "category": model.classes_[index],

                "probability": round(float(probabilities[index] * 100), 2)

            })

        # Helpdesk Information

        ticket_info = HELPDESK_DATA.get(

            prediction,

            {

                "assigned_team": "IT Support",

                "priority": "Medium",

                "eta": "1 Business Day",

                "resolution": [

                    "Please contact the IT Support Team."

                ]

            }

        )

        # Return Response

        return jsonify({

            "prediction": prediction,

            "confidence": confidence,

            "assigned_team": ticket_info["assigned_team"],

            "priority": ticket_info["priority"],

            "eta": ticket_info["eta"],

            "resolution": ticket_info["resolution"],

            "top_predictions": top_predictions

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# -------------------------------------------------------
# Error Handling
# -------------------------------------------------------

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):

    return render_template("500.html"), 500


# -------------------------------------------------------
# Run Application
# -------------------------------------------------------

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )