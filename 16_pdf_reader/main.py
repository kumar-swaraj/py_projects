import re
import sys
from collections import Counter
from os.path import exists

from pypdf import PdfReader


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())
        all_words += [word for word in split_text if len(word) > 2]

    return Counter(all_words)


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    reader = PdfReader(pdf_file)

    print("Pages:", reader.get_num_pages())
    print("-" * 10)

    pdf_text = [page.extract_text() for page in reader.pages]
    return pdf_text


def main() -> None:
    pdf_file_path = "./16_pdf_reader/sample.pdf"  # Default value

    if len(sys.argv) > 1:
        if exists(sys.argv[1]) and sys.argv[0].endswith(".pdf"):
            pdf_file_path = sys.argv[1]
    else:
        file_path = input("Enter pdf file path: ")
        if exists(file_path) and file_path.endswith(".pdf"):
            pdf_file_path = file_path

    extracted_text = extract_text_from_pdf(pdf_file_path)
    counter = count_words(extracted_text)

    for page in extracted_text:
        print(page)

    print("-" * 10, end="\n\n")

    for word, mentions in counter.most_common(5):
        print(f"{word:10}:{mentions:3} times")


if __name__ == "__main__":
    main()
