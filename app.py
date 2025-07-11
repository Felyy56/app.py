import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Tillåt CORS från alla domäner (eller specifika domäner)
CORS(app, origins=["https://visartiden.com", "http://localhost:3000", "https://localhost:3000"])

latest_booking = None

@app.route("/webhook", methods=["POST"])
def webhook():
    global latest_booking
    latest_booking = request.json
    print("Webhook mottagen:", latest_booking)
    return jsonify({"status": "success", "message": "Booking received"}), 200

@app.route("/latest", methods=["GET"])
def latest():
    if latest_booking:
        return jsonify(latest_booking)
    else:
        return jsonify({"message": "Ingen bokning än"}), 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"status": "online", "cors": "enabled"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
