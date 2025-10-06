import csv
from http import HTTPStatus

import requests
from fake_useragent import UserAgent


def format_url(url: str) -> str:
    return url if url.startswith("https://") else f"https://{url}"


def get_websites(csv_path: str):
    """
    Reads a CSV file and returns a generator of formatted website URLs.
    Expects the CSV to have at least two columns per row, with the website URL in the second column (index 1).
    """
    with open(csv_path, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1 and row[1]:
                yield format_url(row[1].strip())


def get_user_agent():
    """Returns a user agent that can be used with requests."""
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int):
    """Uses the status code to return a readable description."""
    try:
        status = HTTPStatus(status_code)
        return f"({status.value} {status.name}) {status.description}"
    except ValueError:
        return "(???) Unknown status code..."


def check_website(website: str, user_agent: str, /):
    """Gets that status code for a website and prints the result."""
    try:
        response = requests.get(website, headers={"User-Agent": user_agent}, timeout=5)
        print(website, get_status_description(response.status_code))
    except requests.exceptions.RequestException as e:
        print(f'** Could not get information for website: "{website}" — {e}')


def main() -> None:
    websites = get_websites("./08_website_checker/websites.csv")
    user_agent = get_user_agent()

    for website in websites:
        check_website(website, user_agent)


if __name__ == "__main__":
    main()
