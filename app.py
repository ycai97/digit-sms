from flask import Flask, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
#
# db = SQLAlchemy(app)
#
# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     msg = db.Column(db.String(), nullable=False)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # # twilio sending msg in
    # if request.method == "POST":
    #     # Get the message the user sent our Twilio number
    #     body = request.values.get('Body', None)
    #     return saveMsg(body)
    # # digit polling last saved msg
    # else:
    #     return getLastSavedMsg()

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return "haha"

def saveMsg(body):
    new_msg = Message(msg=body)
    try:
        db.session.add(new_msg)
        db.session.commit()
        return "Message successfully added to db: " + body
    except:
        return "There was an error adding the message"


def getLastSavedMsg():
    # lastSavedMsg = Message.query.limit(1).all()
    # db.session.delete(lastSavedMsg)
    # db.session.commit()
    # return lastSavedMsg
    return "sss"

if __name__ == "__main__":
    app.run(debug=True)
