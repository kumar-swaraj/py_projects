import qrcode


class MyQR:
    def __init__(self, size: int, padding: int) -> None:
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, filename: str, fg_color: str, bg_color: str):
        user_input = input("Enter text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg_color, back_color=bg_color)
            with open(filename, "wb") as f:
                qr_image.save(f)

            print(f"Successfully created! ({filename})")
        except Exception as e:
            print("Error: ", e)


def main() -> None:
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr(
        "sample.png",
        fg_color="#2A2438",
        bg_color="#DBD8E3",
    )


if __name__ == "__main__":
    main()
