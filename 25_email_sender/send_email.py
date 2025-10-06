import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import credentials


def create_image_attachment(path: str) -> MIMEImage:
    with open(path, mode="rb") as file:
        mime_image = MIMEImage(file.read())
        mime_image.add_header(
            "Content-Disposition", f"attachment; filename={path.lstrip('images/')}"
        )
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = "smtp.gmail.com"
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host=host, port=port) as server:
        print("Logging in...")
        print(server.ehlo())
        server.starttls(context=context)
        print(server.ehlo())
        server.login(user=credentials.EMAIL, password=credentials.PASSWORD)

        # Prepare the email
        print("Attempting to send the email")
        message = MIMEMultipart()
        message["from"] = credentials.EMAIL
        message["to"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if image is not None:
            file: MIMEImage = create_image_attachment(path=image)
            message.attach(file)

        server.sendmail(
            from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string()
        )

        # Success!
        print("Sent!")


if __name__ == "__main__":
    send_email(
        to_email="TO_EMAIL",
        subject="Hey there",
        body="This is body of email.",
        image="images/alex-moliski-A_-lP_V7WJ0-unsplash.jpg",
    )
