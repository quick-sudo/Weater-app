from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def temp():
    city = 'Рязань' # Указываем интересующий город
    appid = 'api_key' # Указываем ключ, полученный при регистрации на OpenWeatherMap.org
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={appid}'
    
    try:
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        
        return f'Сейчас в городе {city} {temperature} °C<br>Ощущается как {temperature_feels} °C'
    except Exception as e:
        return f'Ошибка получения данных: {str(e)}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)