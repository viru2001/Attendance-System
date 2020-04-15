
'''import os
from twilio.rest import Client

client = Client()
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+8291105704'
client.messages.create(body='hii viresh',
                       from_ = from_whatsapp_number,
                        to = to_whatsapp_number)'''



# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def sending_msg(l):
    account_sid = 'AC33d091e217ab0caf0659e1339dd8ab9b'
    auth_token = '265b9ad2f451cef592b7a610df1f9698'
    client = Client(account_sid, auth_token)
    msg = "Hello,"+"\n"+l[0]+"\n"+"Your attendance of subject -> *"+l[3][0]+"* and month -> *"+l[3][1]+"* is : *"+l[1]+"*%"
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=msg,
                                  to='whatsapp:'+l[2]
                              )
    #print(message.sid)
    print("msg sent")


def sending_msg1(l,sm):
    account_sid = 'AC33d091e217ab0caf0659e1339dd8ab9b'
    auth_token = '265b9ad2f451cef592b7a610df1f9698'
    client = Client(account_sid, auth_token)
    n=len(l)
    msg = "Defaulter List of Subject -> *" + sm[0] + "* and Month -> *" + sm[1] + "* is : \n"
    for i in range(n):
        msg += l[i][0] +"  "+l[i][1]+"   "+l[i][2]+"%\n"

    #print(msg)

    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=msg,
                                  to='whatsapp:+918291105704'
                              )
    #print(message.sid)
    print("msg sent")