import requests


def get_weather(location: str):
    url = f'http://wttr.in/{location}?nTqM&lang=ru'
    response: requests.Response = requests.get(url)
    response.raise_for_status()
    return response.content.decode('utf-8')


def get_weather_for_locations(locations: list):
    for location in locations:
        print(get_weather(location))


def main():
    locations = ['Шереметьево', 'London', 'Череповец']
    get_weather_for_locations(locations)


if __name__ == '__main__':
    main()
