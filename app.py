from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

DATA = []

# Load CSV
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        DATA.append(row)

@app.route("/")
def home():
    return "API LIVE ✅"

@app.route("/api/numinfo")
def api():
    key = request.args.get("key")
    num = request.args.get("num")

    if key != "Anonymous":
        return jsonify({"status": "error", "message": "Invalid API Key"})

    for row in DATA:
        if row["number"] == num:
            return jsonify({
                "status": "success",
                "data": row,
                "powered_by": "Vernex 🔥"
            })

    return jsonify({
        "status": "not_found",
        "message": "No data found"
    })
