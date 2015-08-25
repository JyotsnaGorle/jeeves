from strategies import play_music.PlayMusic
from strategies import start_tv.StartTV
from strategies import order_pizza.OrderPizza
from strategies import order_food.OrderFood
from strategies import open_facebook.OpenFacebook
from strategies import control_ac.ControlAC
from strategies import control_fan.ControlFan
from strategies import suggest_restaurant.SuggestRestaurant
from strategies import make_coffee.MakeCoffee
from strategies import suggest_recipe.SuggestRecipe

strategies = {
    "feel": {
        "bored": [PlayMusic(), StartTV()],
        "hungry": [OrderPizza(), OrderFood()],
        "lonely": [OpenFacebook()],
        "hot": [ControlAC()],
        "warm": [ControlAC(), ControlFan()],
        "cold": [ControlAC()]
    },
    "need": {
        "music": [PlayMusic()],
        "food": [SuggestRestaurant(), SuggestRecipe()],
        "coffee": [MakeCoffee()]
    }
}

class Strategies:
    def get_strategies(self):
        return strategies
