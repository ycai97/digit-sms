from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
msg_list = []

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
        msg_list.append(body)
        return str(resp)
    # digit polling last saved msg
    else:
        try:
            return msg_list[-1]
        except:
            return ""


if __name__ == "__main__":
    app.run(debug=True)
