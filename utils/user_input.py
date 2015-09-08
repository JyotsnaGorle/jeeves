from chat_ui import communicator

def user_input(message):
    reply = raw_input(message)
    communicator.send_to_ui('{"person": "%s", "msg": "%s"}' % ("user", reply))
    return reply
