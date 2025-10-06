import json
from typing import Any, Final, cast

import requests
from model import Weather, dt

BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY: Final[str] = "YOUR KEY"


def get_weather(cityname: str, mock: bool = True):
    if mock:
        print("Using mock data...")

        with open("26_weather_app/dummy_data.json") as file:
            return json.load(file)

    payload: dict[str, str] = {
        "q": cityname,
        "appid": API_KEY,
        "units": "metric",
    }
    response = requests.get(BASE_URL, payload)
    return response.json()


def get_weather_details(weather: dict[Any, Any]) -> list[Weather]:
    days: list[dict[Any, Any]] = cast(Any, weather.get("list"))
    if not days:
        raise Exception(f"Problem with json: {weather}")

    list_of_weather: list[Weather] = []
    for day in days:
        w = Weather(
            date=dt.fromtimestamp(day.get("dt")),  # type: ignore
            details=(details := day.get("main")),  # type: ignore
            temp=details.get("temp"),  # type: ignore
            weather=(weather := day.get("weather")),  # type: ignore
            description=weather[0].get("description"),
        )
        list_of_weather.append(w)

    return list_of_weather
