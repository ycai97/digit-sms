from flask import Flask, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

msg_list = []
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'

# db = SQLAlchemy(app)
#
# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     msg = db.Column(db.String(), nullable=False)

# db.create_all()
# db.session.commit()

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # twilio sending msg in
    if request.method == "POST":
        # Get the message the user sent our Twilio number
        body = request.values.get('Body', None)
        resp = MessagingResponse()
        resp.message("The Robots are coming! Head for the hills!")
        # saveMsg(body)

        msg_list.append(body)
        return str(resp)
    # digit polling last saved msg
    else:
        try:
            return msg_list[-1]
        except:
            return ""

    # # Start our TwiML response
    # resp = MessagingResponse()
    #
    # # Add a message
    # resp.message("The Robots are coming! Head for the hills!")
    #
    # return str(resp)

#
# def saveMsg(body):
#     new_msg = Message(msg=body)
#     print(new_msg)
#     try:
#         db.session.add(new_msg)
#         db.session.commit()
#     except:
#         pass


# def getLastSavedMsg():
#     try:
#         lastSavedMsg = Message.query.limit(1).first()
#         print(lastSavedMsg)
#         db.session.delete(lastSavedMsg)
#         db.session.commit()
#         return str(lastSavedMsg.msg)
#     except:
#         return ""

if __name__ == "__main__":
    app.run(debug=True)
