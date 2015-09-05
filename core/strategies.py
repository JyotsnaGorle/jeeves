from .strategy_impl.control_ac import ControlAC
from .strategy_impl.control_fan import ControlFan
from .strategy_impl.make_coffee import MakeCoffee
from .strategy_impl.open_facebook import OpenFacebook
from .strategy_impl.order_food import OrderFood
from .strategy_impl.play_music import PlayMusic
from .strategy_impl.read_news_and_weather import ReadNewsAndWeather
from core.strategy_impl.play_animal_game import PlayAnimalGame
from core.strategy_impl.read_emails import ReadEmails
from core.strategy_impl.speech_response import SpeechResponse

strategies = {
    "feel": {
        "bored": [PlayAnimalGame(), PlayMusic()],
        "cold": [ControlAC()],
        "hot": [ControlAC()],
        "hungry": [OrderFood()],
        "lonely": [OpenFacebook()],
        "love": [SpeechResponse("love")],
        "sleepy": [SpeechResponse("sleepy")],
        "tired": [SpeechResponse("tired")],
        "warm": [ControlAC(), ControlFan()]
    },
    "need": {
        "coffee": [MakeCoffee()],
        "emails": [ReadEmails()],
        "food": [OrderFood()],
        "mails": [ReadEmails()],
        "news": [ReadNewsAndWeather()]
    }
}
