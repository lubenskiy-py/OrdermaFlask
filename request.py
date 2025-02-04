import requests
from translate import Translator



request = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=49.0147974360402&lon=35.363718658364675&appid=3d091ec94e3b0797e797bfbf6c4f4a40&units=metric').json()
translator= Translator(from_lang="english", to_lang="ukrainian")
translate_weather = translator.translate(request["weather"][0]["main"])