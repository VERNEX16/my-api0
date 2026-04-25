from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Shayan API LIVE 🚀"

@app.route("/api/numinfo")
def numinfo():
    key = request.args.get("key")
    num = request.args.get("num")

    # 🔐 Your API key
    if key != "Anonymous":
        return jsonify({
            "status": "error",
            "message": "Invalid API key"
        })

    # 🔗 External API (background)
    external_url = "https://cyber-osint-num-infos.vercel.app/api/numinfo"

    params = {
        "key": "Anonymous",
        "num": num
    }

    try:
        res = requests.get(external_url, params=params, timeout=10)
        data = res.json()

        # 🔁 Return with your branding
        return jsonify({
            "status": data.get("status"),
            "data": data.get("data"),
            "powered_by": "Shayan API 🚀"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "API failed",
            "error": str(e)
        })
