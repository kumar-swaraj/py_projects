from typing import Optional

import requests


def download_image(image_url: str, folder_name: Optional[str]) -> None:
    try:
        with requests.get(image_url, stream=True) as response:
            response.raise_for_status()

            if response.ok:
                if file_name := response.headers.get("content-disposition"):
                    file_name = file_name.removeprefix("attachment;filename=").strip(
                        '"'
                    )
                else:
                    file_name = input("What would you like to name it?: ")

                if folder_name:
                    file_path = rf"{folder_name}/{file_name}"
                else:
                    file_path = file_name

                with open(file_path, mode="wb") as file:
                    print("downloading...")
                    for chunk in response.iter_content():
                        file.write(chunk)
                print(f"File downloaded successfully to: {file_path}")
            else:
                print("response is not ok", response.status_code)

    except requests.exceptions.HTTPError as e:
        print("Error downloading the file:", e)


def main() -> None:
    input_url: str = input("Enter a downloadable image url: ")

    download_image(input_url, "images")


if __name__ == "__main__":
    main()
