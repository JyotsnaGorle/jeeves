# Jeeves


**"*Inspired by the various automation and intelligent assistants out there and the Almighty himself, Jeeves is the invisible, omnipotent and benevolent deity watching over all of us and helping us out in times of need and forgiveness. Unlike the other omnipotent & benevolent deities up there in the heavens, your prayers actually do get answered and with a little twist too.*"**

---------------------------------

## Prerequisites to attain nirvana
- *NIX System. Windows won't be supported. Swear.
- Python 2.7.x (Python 3 compatibility coming soon) (https://www.python.org/downloads/)
- pip (https://pip.pypa.io/en/latest/installing.html).
- RPi.GPIO (>= 0.5.11) python module on the RaspberryPi for GPIO h/w interfacing.
- C/C++ build tool chains like gcc/clang for building native python modules.
- espeak for Linux variants and say TTS engines for mac

## Running the Almighty

- Clone this repo using  ``` git clone https://github.com/rahul080327/jeeves.git ```
- While inside the cloned folder jeeves, follow the following commandments:
    - sudo pip install -U -r requirements.txt
    - (optional - to control h/w) (on the Raspberry Pi) sudo pip install -U RPi.GPIO
    - log into the python REPL and run
        - import nltk
        - nltk.download()
        - Select 'all' from the manager and hit download and take a coffee break.
    - run jeeves as: ``` python jeeves.py [-h] [--input INPUT] [--host HOST] [--port PORT] ```
    - [deprecated] run jeeves as read from stdin mode: ``` python jeeves.py ```
    - run jeeves as read from mic mode using Google's speech recognizer: ``` python jeeves.py --input mic ```
    - run jeeves as read from mic mode using Julius H/W speech recognizer:  coming soon
    - run jeeves as read from mic mode using CMU PocketSphinx H/W speech recognizer:  coming soon
    - To control actual hardware via Raspberry Pi, make sure jeeves and the RasPi are on the same subnet and rechable, note down RasPi's IP address and edit **line number 3 in utils/connect_to_hw_server.py** and restart.
    - To make the RasPi/RasPi2 hardware aware, Figure out the pin layouts and the corresponding h/w you want to connect at the specified GPIO pins from https://www.raspberrypi.org/documentation/usage/gpio/. Then copy the file in rpi_server/hw_router.py onto the Pi. Edit the corresponding pins and device names in the fle and run it using ``` sudo python hw_router.py ```. **sudo is mandatory here.**

## Contributing
Jeeves is licensed under the The BSD 3-Clause License which means all you folks are free to use this in any of your projects/products and we will be grateful for any and every contributions. Thanks in advance!

# P.G. Wodehouse would've been proud of me.
