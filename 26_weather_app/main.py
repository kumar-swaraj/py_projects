from weather_api import Weather, get_weather, get_weather_details


def main() -> None:
    user_city = input("Enter a city: ")

    current_weather = get_weather(user_city, True)
    weather_details = get_weather_details(current_weather)

    dtfmt: str = "%d/%m/%y"
    days = sorted({f"{date.date:{dtfmt}}" for date in weather_details})

    for day in days:
        print(day)
        print("---")

        # Group the weather data by date to make it easier to read
        grouped: list[Weather] = [
            current for current in weather_details if f"{current.date:{dtfmt}}" == day
        ]
        for element in grouped:
            print(element)

        print()  # An empty line


if __name__ == "__main__":
    main()
