from flask import Flask, jsonify, request
from flask_cors import CORS
from models.diabetes_model import predict_diabetes

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return "This is amit"


@app.route('/api/diabetes', methods=['GET', 'POST'])
def predict():
    try:
        input_array = request.json
        someNumber = predict_diabetes([6, 160, 23, 14, 9, 29, 55])
        return jsonify({'data': someNumber})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
