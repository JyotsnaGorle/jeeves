from core.strategy_impl.play_animal_game import PlayAnimalGame
from core.strategy_impl.read_emails import ReadEmails
from core.strategy_impl.speech_response import SpeechResponse
from .strategy_impl.play_music import PlayMusic
from .strategy_impl.order_food import OrderFood
from .strategy_impl.open_facebook import OpenFacebook
from .strategy_impl.control_ac import ControlAC
from .strategy_impl.control_fan import ControlFan
from .strategy_impl.make_coffee import MakeCoffee
from .strategy_impl.read_news_and_weather import ReadNewsAndWeather

strategies = {
    "feel": {
        "bored": [PlayAnimalGame()],
        "hungry": [OrderFood()],
        "lonely": [OpenFacebook()],
        "hot": [ControlAC()],
        "warm": [ControlAC(), ControlFan()],
        "cold": [ControlAC()],
        "tired": [SpeechResponse("tired")],
        "sleepy": [SpeechResponse("sleepy")],
        "love": [SpeechResponse("love")],
    },
    "need": {
        "food": [OrderFood()],
        "coffee": [MakeCoffee()],
        "news": [ReadNewsAndWeather()],
        "emails": [ReadEmails()],
        "mails": [ReadEmails()],
    }
}
