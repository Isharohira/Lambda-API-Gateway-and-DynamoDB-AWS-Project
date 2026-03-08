from flask import Flask, request, send_file
import boto3

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return send_file("contactus.html")

@app.route("/contact", methods=["POST"])
def contact():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    message = request.form.get("message")

    client = boto3.client('dynamodb')

    client.put_item(
        TableName='ishatable',
        Item={
            'email': {'S': email},
            'fname': {'S': fname},
            'lname': {'S': lname},
            'message': {'S': message}
        }
    )

    return send_file("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
