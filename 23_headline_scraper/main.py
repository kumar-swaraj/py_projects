import requests
from bs4 import BeautifulSoup


def get_soup(url: str = "https://www.bbc.com/news") -> BeautifulSoup:
    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)  # headers is optional
    html: bytes = response.content
    soup = BeautifulSoup(html, "html.parser")

    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set[str] = set()

    for h in soup.find_all("h2", attrs={"data-testid": "card-headline"}):
        headline = h.contents[0].get_text().lower()
        headlines.add(headline)

    return sorted(headlines)


def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(
                f'{i}: {headline.capitalize()} <----------------------------- "{term}"'
            )
        else:
            print(f"{i}: {headline.capitalize()}")

    print("----------------------------------")
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times.')
        print("----------------------------------")

        for i, headline in enumerate(term_list, start=1):
            print(f"{i}: {headline.capitalize()}")
    else:
        print(f'No matches found for: "{term}"')
        print("----------------------------------")


def main() -> None:
    soup = get_soup()
    headlines = get_headlines(soup)

    user_input: str = input("What term would you like to check for? >> ")
    check_headlines(headlines, user_input)


if __name__ == "__main__":
    main()
