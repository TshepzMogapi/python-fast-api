import logging
from typing import Dict

from dotenv import find_dotenv
from dotenv import load_dotenv

# from sendgrid.helpers.mail import Mail

# import os
# from sendgrid import SendGridAPIClient

dotenv_file = find_dotenv()

load_dotenv(dotenv_path=dotenv_file)
dotenv_file = find_dotenv()


# message = Mail(
#     from_email="from_email@example.com",
#     to_emails="to@example.com",
#     subject="Sending with Twilio SendGrid is Fun",
#     html_content="<strong>and easy to do anywhere, even with Python</strong>",
# )


def send_email(email_body: Dict):
    try:
        logging.info("sendign email")
        # sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        # response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(str(e))
