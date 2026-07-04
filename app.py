from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import os

app = Flask(__name__)
CORS(app)

model = load("phishing_model.pkl")
vectorizer = load("vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")

    vec = vectorizer.transform([url])
    prediction = model.predict(vec)[0]

    return jsonify({
        "is_phishing": int(prediction),
    })

if __name__ == "__main__":
    app.run(debug=True)
