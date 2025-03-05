from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.mailUtils import sendmail

app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": "https://shivrajkolwankar.netlify.app","https://shivraj-kolwankar.netlify.app",
            "methods": "POST",
            "allow_headers": "Content-Type",
        }
    },
)


@app.route("/api/contactUs", methods=["POST"])
def contact_us():
    try:
        data = request.json
        email = data.get("email")
        name = data.get("name")
        message = data.get("message")
        sendmail(name, email, message)
        return jsonify({"status": True, "message": "Message sent successfully!"})
    except Exception as err:
        return jsonify({"status": False, "message": str(err)})


if __name__ == "__main__":
    app.run(port=3000)
