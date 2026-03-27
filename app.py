from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(port=5000)