from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from gmail import fetch_emails  # Import the fetch_emails function

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/submit_gmail', methods=['POST'])
def submit_gmail():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Extract email and password from the request
    email = data.get('email')
    password = data.get('password')

    # Check if email and password were provided
    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password are required!"}), 400

    # Call the fetch_emails function to get the email data
    email_data = fetch_emails(email, password)

    # If fetching emails failed (check for error in JSON response), return it directly
    if "error" in email_data:
        return Response(email_data, status=500, mimetype='application/json')

    # Return the fetched email data directly as JSON
    return Response(email_data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
