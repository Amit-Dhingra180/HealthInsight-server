from flask import Flask, jsonify, request
from flask_cors import CORS
from models.diabetes_model import predict_diabetes
from models.heart_model import predict_heart

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return "This is amit"


@app.route('/api/diabetes', methods=['GET', 'POST'])
def predict():
    try:
        input_array = request.json
        someNumber = predict_diabetes(input_array)
        return jsonify({'data': someNumber})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

@app.route('/api/heart', methods=['POST'])
def predict_heart_data():
    try:
        input_data = request.json
        prediction = predict_heart(input_data)
        return jsonify({'data': prediction})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
