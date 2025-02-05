import requests
from translate import Translator



response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=49.013548340248036&lon=35.348341572571165&appid=3d091ec94e3b0797e797bfbf6c4f4a40&units=metric').json()
translator = Translator(from_lang="english", to_lang="ukrainian")
translate_weather = translator.translate(response["weather"][0]["main"])