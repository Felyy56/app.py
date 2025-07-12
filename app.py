import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Lägg till din lokala utvecklingsserver i CORS
CORS(app, origins=[
    "http://localhost:3000", 
    "https://localhost:3000",
    "http://127.0.0.1:5500",  # ← LÄGG TILL DENNA
    "http://localhost:5500",  # ← OCH DENNA FÖR SÄKERHETS SKULL
    "http://localhost:8080",  # ← VANLIG UTVECKLINGSPORT
    "http://127.0.0.1:8080"   # ← OCH DENNA
    "http://127.0.0.1:8080"   # ← OCH DENNA
])

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
