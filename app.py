# 2. Updated `app.py`

from flask import Flask, jsonify, request

app = Flask(__name__)

# Main page
@app.route('/')
def home():
    return "<h1>Welcome to Django_project1!</h1><p>This is a simple Flask application running in a Docker container.</p>"

# API - simple API sample
@app.route('/api/v1/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

# API - Return application information
@app.route('/api/v1/info', methods=['GET'])
def app_info():
    return jsonify({
        "app_name": "Django_project1",
        "version": "1.0.0",
        "description": "A simple Flask application for CI/CD demonstration."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
