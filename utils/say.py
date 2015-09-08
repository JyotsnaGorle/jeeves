from subprocess import call
from chat_ui import communicator

import platform

def say(what):
    command = {
        "Darwin": "say",
        "Linux": "espeak"
    }[platform.system()]

    call([command, what])
    communicator.send_to_ui("jeeves", what)
