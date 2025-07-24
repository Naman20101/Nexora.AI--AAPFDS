from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Nexora.AI Ready (2025)"

@app.route('/api/predict', methods=['POST'])
def predict():
    return jsonify({"fraud": False})  # Replace with your model later

if __name__ == '__main__':
    app.run()
