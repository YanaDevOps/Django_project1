from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Main page route
@app.route('/')
def home():
    # Render the index.html template when the home route is accessed
    return render_template('index.html')

# API - simple API example
@app.route('/api/v1/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the request, default to 'Guest'
    name = request.args.get('name', 'Guest')
    # Return a JSON response with a greeting message
    return jsonify({"message": f"Hello, {name}!"})

# API - Return application information
@app.route('/api/v1/info', methods=['GET'])
def app_info():
    # Return a JSON response with app details
    return jsonify({
        "app_name": "Python_project_1",
        "version": "1.0.0",
        "description": "A simple Flask application for CI/CD demonstration."
    })

if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
