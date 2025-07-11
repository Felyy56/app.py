from flask import Flask, request, jsonify

app = Flask(__name__)
latest_booking = None

@app.route("/webhook", methods=["POST"])
def webhook():
    global latest_booking
    latest_booking = request.json
    print("Webhook mottagen:", latest_booking)
    return "OK", 200

@app.route("/latest", methods=["GET"])
def latest():
    if latest_booking:
        return jsonify(latest_booking)
    else:
        return "Ingen bokning än", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
