import json
from typing import Final, cast

import requests

BASE_URL: Final[str] = "https://api.frankfurter.dev/v1/latest"


def get_rates(mock: bool = False):
    """Get the current rates from a currency api."""

    if mock:
        with open("./22_currency_converter/rates.json", mode="r") as file:
            return json.load(file)

    payload: dict[str, str] = {
        "amount": "1",
        "base": "USD",
    }
    response = requests.get(url=BASE_URL, params=payload)
    data = response.json()

    return data


def get_currency(currency: str, rates: dict[str, float]):
    """Get the exchange rate for the specified currency if it exists."""

    if currency.upper() in rates:
        return rates.get(currency)
    else:
        raise ValueError(f"{currency} is not a valid currency")


def convert_currency(
    amount: float, base: str, vs: str, rates: dict[str, float]
) -> float:
    """Convert the base currency to the vs currency at the given rate."""

    vs_rate = get_currency(vs, rates)
    vs_rate = cast(float, vs_rate)

    conversion: float = round((vs_rate) * amount, 2)
    print(f"{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})")
    return conversion


def main() -> None:
    data = get_rates()
    rates = data.get("rates")

    convert_currency(10, base="USD", vs="INR", rates=rates)


if __name__ == "__main__":
    main()
