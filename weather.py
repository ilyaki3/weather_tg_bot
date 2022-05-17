from config import API_TOKEN
import requests


# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}


def get_today_weather(location, period, API_TOKEN):
    # part = 'current, minutely, hourly, alerts'
    cnt = 40
    try:

        r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?'
                         f'lat={location["latitude"]}&lon={location["longitude"]}'
                         f'&cnt={cnt}&appid={API_TOKEN}&units=metric&lang=ru')
        data = r.json()
        # pprint(data)
        if period == '/Сегодня':
            weather = {
                'city': data['city']['name'],
                'date': data['list'][0]['dt_txt'],
                'weather': data['list'][4]['weather'][0]['description'],
                'temp_max': data['list'][4]['main']['temp_max'],
                'temp_min': data['list'][1]['main']['temp_min'],
            }

            result = f"Сегодня {weather['date'][:10]} в {weather['city']}\n"\
                     f"{weather['weather']}\n"\
                     f"Температура днем {weather['temp_max']} C\n" \
                     f"Температура ночью {weather['temp_min']} C"
            # pprint(result)
            return result

        elif period == '/Завтра':
            weather = {
                'city': data['city']['name'],
                'date': data['list'][8]['dt_txt'],
                'weather': data['list'][12]['weather'][0]['description'],
                'temp_max': data['list'][12]['main']['temp_max'],
                'temp_min': data['list'][9]['main']['temp_min'],
            }

            result = f"Завтра {weather['date'][:10]} в {weather['city']}\n" \
                     f"{weather['weather']}\n" \
                     f"Температура днем {weather['temp_max']} C\n" \
                     f"Температура ночью {weather['temp_min']} C"
            # pprint(result)
            return result

    except Exception as ex:
        print(ex)

# get_today_weather(location, API_TOKEN)