from subprocess import call

import platform

def say(what):
    command = {
        "Darwin": "say",
        "Linux": "espeak"
    }[platform.system()]

    call([command, what])
