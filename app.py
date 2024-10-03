# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# from gmail import fetch_emails  # Import the function from gmail.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from gmail import fetch_emails  # Import the function from gmail.py

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

    # Call the function to fetch emails and return JSON data
    email_data = fetch_emails(email, password)

    # If fetching emails failed (e.g., login failed), return an error
    if "error" in email_data:
        return jsonify(json.loads(email_data)), 500

    # Return the fetched email data in JSON format
    return jsonify(json.loads(email_data))

if __name__ == '__main__':
    app.run(debug=True)


# import io

# app = Flask(__name__)
# CORS(app)
# @app.route('/')
# def home():
#     return "Hello, World!"
# @app.route('/submit_gmail', methods=['POST'])
# def submit_gmail():
#     # Get the JSON data from the POST request
#     data = request.get_json()

#     # Extract email and password from the request
#     email = data.get('email')
#     password = data.get('password')

#     # Check if email and password were provided
#     if not email or not password:
#         return jsonify({"status": "error", "message": "Email and password are required!"}), 400

#     # Call the function to generate the PDF in memory
#     pdf_output = fetch_emails(email, password)

#     # If PDF generation failed (e.g., login failed), return an error
#     if pdf_output is None:
#         return jsonify({"status": "error", "message": "Failed to process request!"}), 500

#     # Send the PDF as a downloadable file
#     return send_file(pdf_output, as_attachment=True, download_name="emails.pdf", mimetype='application/pdf')

# if __name__ == '__main__':
#     app.run(debug=False)


# # from flask import Flask, request, jsonify, send_file
# # from flask_cors import CORS
# # from gmail import getMailsAndMakePDF  # Import the function from gmail.py
# # import io

# # app = Flask(__name__)
# # CORS(app)

# # @app.route('/submit_gmail', methods=['POST'])
# # def submit_gmail():
# #     # Get the JSON data from the POST request
# #     data = request.get_json()

# #     # Extract email and password from the request
# #     email = data.get('email')
# #     password = data.get('password')

# #     # Check if email and password were provided
# #     if not email or not password:
# #         return jsonify({"status": "error", "message": "Email and password are required!"}), 400

# #     # Call the function to generate the PDF in memory
# #     pdf_output = getMailsAndMakePDF(email, password)

# #     # If PDF generation failed (e.g., login failed), return an error
# #     if pdf_output is None:
# #         return jsonify({"status": "error", "message": "Failed to process request!"}), 500

# #     # Send the PDF as a downloadable file
# #     return send_file(pdf_output, as_attachment=True, download_name="emails.pdf", mimetype='application/pdf')

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # app = Flask(__name__)
# # from gmail import getMailsAndMakePDF
# # CORS(app)
# # @app.route('/submit_gmail', methods=['POST'])
# # def submit_gmail():
# #     data = request.get_json()
# #     email = data.get('email')
# #     password = data.get('password')
# #     getMailsAndMakePDF(email, password)
# #     # Here you can process the email and password
# #     # Example: saving them to a database, validation, etc.
    
# #     print(f"Received Email: {email}")
# #     print(f"Received Password: {password}")
    
# #     return jsonify({"status": "success", "message": "Data received!"})

# # if __name__ == '__main__':
# #     app.run(debug=True)


# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from gmail import fetch_emails_and_generate_pdf  # Import the function

# # app = Flask(__name__)
# # CORS(app)

# # @app.route('/submit_gmail', methods=['POST'])
# # def submit_gmail():
# #     data = request.get_json()
# #     email = data.get('email')
# #     password = data.get('password')
    
# #     # Log the received email and password
# #     print(f"Received Email: {email}")
# #     print(f"Received Password: {password}")

# #     # Call the function to fetch emails and generate PDF
# #     try:
# #         fetch_emails_and_generate_pdf(email, password)  # Call the function
# #         return jsonify({"status": "success", "message": "Emails fetched and PDF generated!"})
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         return jsonify({"status": "error", "message": "Failed to fetch emails and generate PDF."})

# # if __name__ == '__main__':
# #     app.run(debug=True)
