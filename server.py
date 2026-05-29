from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your index.html file to safely request data from this server

MOCK_DATA = {
    "site_status": "Active",
    "developer_role": "WordPress & Automation Engineer",
    "location_node": "Cameroon Local Host",
    "completed_lessons": [1, 2, 3, 4]
}

@app.route('/', methods=['GET'])
def home_endpoint():
    return jsonify(MOCK_DATA)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)