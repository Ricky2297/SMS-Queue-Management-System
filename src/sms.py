import os
from twilio.rest import Client

def send(body='Some body', to=''):
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = 'AC2336944065089e1362000959ac1a6470'
    auth_token = 'cd3902e55ad90cc4ce292fdc646effab'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='your table is ready',
        from_='+17205732070',
        to='+17862414331'
    )

    print(message.sid)