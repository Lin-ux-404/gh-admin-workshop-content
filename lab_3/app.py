# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


# Simple health check that's great for CI
@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


# A tiny business endpoint: sums two numbers
@app.get("/sum")
def sum_api():
    """
    Example:
    GET /sum?a=2&b=3  -> {"result": 5}
    """
    # Defensive parsing with defaults
    a = request.args.get("a", None)
    b = request.args.get("b", None)

    # Validate inputs

    try:
        a = int(a) if a is not None else 0
        b = int(b) if b is not None else 0
    except ValueError:
        return jsonify({"error": "a and b must be integers"}), 400

    return jsonify({"result": a + b}), 200


if __name__ == "__main__":
    # Local dev run: `python app.py`
    app.run(host="0.0.0.0", port=5000, debug=True)
