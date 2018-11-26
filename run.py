# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.messaging_response import Message
import datetime

app = Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Your time has been recorded as " + str(datetime.datetime.now()))

    return str(resp)

# @app.route("/incoming", methods=['GET', 'POST'])
# def incoming_msg():
#     msg = Message.body()
#     return str(msg)


if __name__ == "__main__":
    app.run(debug=True)
