import requests


def get_weather(location: str):
    params = {
        'nTqM': '',
        'lang': 'ru'
        }

    url = f'http://wttr.in/{location}'
    response: requests.Response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = ['Шереметьево', 'London', 'Череповец']
    for location in locations:
        print(get_weather(location))


if __name__ == '__main__':
    main()
