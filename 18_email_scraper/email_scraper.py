import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX: Final[
    str
] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class EmailScraper:
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-extension")
        options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(options=options)

    def scrape(self, url: str) -> set[str]:
        self.driver.get(url)

        print(f"Scrapping: {self.driver.title}")

        page_source = self.driver.page_source
        set_of_emails: set[str] = set()

        for re_match in re.finditer(EMAIL_REGEX, page_source):
            set_of_emails.add(re_match.group())

        return set_of_emails

    def close(self) -> None:
        self.driver.quit()


def main() -> None:
    email_scrapper = EmailScraper()
    emails = email_scrapper.scrape("https://www.randomlists.com/email-addresses?qty=50")
    email_scrapper.close()

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=": ")


if __name__ == "__main__":
    main()
