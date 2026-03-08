from flask import Flask, request, send_file
import boto3

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def home():
    return send_file("contactus.html")


# Contact route
@app.route("/contact", methods=["GET", "POST"])
def contact():

    # If someone directly opens /contact
    if request.method == "GET":
        return send_file("contactus.html")

    # Form data
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    message = request.form.get("message")

    # Connect to DynamoDB
    client = boto3.client(
        "dynamodb",
        region_name="ap-south-1"
    )

    # Insert data into table
    client.put_item(
        TableName="ishatable",
        Item={
            "email": {"S": email},
            "fname": {"S": fname},
            "lname": {"S": lname},
            "message": {"S": message}
        }
    )

    return send_file("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
