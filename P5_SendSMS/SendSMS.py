# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC937222e1f5f62b4c2dafXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "9374634ff8fd98eb30d2b9XXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15136418755", 
    from_="+18598881756",
    body="Hello from Python!")

print(message.sid)
