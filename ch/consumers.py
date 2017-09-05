import json
from channels import Group
from channels.sessions import channel_session

# Connected to websocket.connect
@channel_session
def ws_connect(message, key):
    # Accept connection
    message.reply_channel.send({"accept": True})

# Connected to websocket.receive
@channel_session
def ws_message(message, key):
    reply = json.dumps({'status':'ok'})
    message.reply_channel.send({"text": reply})

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message, key):
    message.reply_channel.send({'accept': False})