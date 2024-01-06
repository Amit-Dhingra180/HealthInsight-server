from flask import Flask, jsonify, request
from flask_cors import CORS
from hello_logic import say_hello_logic  # Import the logic function

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "This is amit"

@app.route('/api/say-hello', methods=['POST'])
def say_hello():
    input_data = request.json
    user_input = input_data.get('input', '')

    output = say_hello_logic(user_input)

    result = {'output': output}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
