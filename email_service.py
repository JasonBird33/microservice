import os
import time
import smtplib
from email.message import EmailMessage

IO_FOLDER = "io"
INPUT_FILE = os.path.join(IO_FOLDER, "email-service.txt")

SMTP_SERVER = "smtp.ethereal.email"
SMTP_PORT = 587
EMAIL_ADDRESS = "lonzo.ohara@ethereal.email"
EMAIL_PASSWORD = "CwfsUNH4czefr77Ke2"

def send_email(recipient_email, tracking_number):
    msg = EmailMessage()
    msg['Subject'] = f"Package {tracking_number} Delivered"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg.set_content(f"Hello,\n\nYour package with tracking number {tracking_number} has been delivered!\n\nThank you.")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def watch_for_delivery():
    print("Email service running...")

    while True:
        if os.path.exists(INPUT_FILE):
            with open(INPUT_FILE, 'r') as f:
                data = f.read().strip()
            os.remove(INPUT_FILE)

            response_path = os.path.join(IO_FOLDER, "email-response.txt")

            if data:
                try:
                    track_num, email = data.split("|")
                    send_email(email, track_num)
                    with open(response_path, "w") as r:
                        r.write(f"SUCCESS: Email sent for package {track_num} to {email}")
                    print(f"Sent delivery email for package {track_num} to {email}")
                except Exception as e:
                    with open(response_path, "w") as r:
                        r.write(f"ERROR: {str(e)}")
                    print("Error sending email:", e)
        time.sleep(1)


if __name__ == "__main__":
    watch_for_delivery()
