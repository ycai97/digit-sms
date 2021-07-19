from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
msg_str = ""

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # twilio sending msg in
    if request.method == "POST":
        # Get the message the user sent our Twilio number
        body = request.values.get('Body', None)
        # Automatic reply
        resp = MessagingResponse()
        resp.message("ON IT BOSS :)")
        # Append operator response to list
        msg_str = body
        return str(resp)
    # digit polling last saved msg
    else:
        temp = msg_str
        # Reinitialize string after each poll
        msg_str = ""
        return temp


if __name__ == "__main__":
    app.run(debug=True)
