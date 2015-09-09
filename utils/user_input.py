from chat_ui import communicator
from google_speech_api.recognizer import recognize

def user_input(message):
    reply = recognize()
    communicator.send_to_ui("user", reply)
    return reply
