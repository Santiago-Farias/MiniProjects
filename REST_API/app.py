from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch users'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)