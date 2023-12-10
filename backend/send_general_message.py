from email.mime.multipart import MIMEMultipart

import requests
import json
import smtplib
from email.mime.text import MIMEText

API_KEY = ""
API_PATH = "https://api.openai.com/v1/chat/completions"
SENDER = "vlad.ionescu@eestec.ro"
MAIL_PASSWORD = ""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def write_message(receiver_type, receiver_name, product_name, percentage):
    if receiver_type == "customer":
        prompt = f"Give me a short whatsapp message for a customer of my company, RetailX, saying there is a {percentage}% discount for {product_name} for 48 hours. Make it personal. Customer's name is {receiver_name}."
    else:
        prompt = f"Give me a short message for one of my employees at RetailX to suggest raising stock of product {product_name} by {percentage}%, as the request will be increasing. Employee's name is {receiver_name}."

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    generated_text = requests.post(url=API_PATH, headers=headers, data=json.dumps(payload))
    return generated_text.json()["choices"][0]["message"]["content"]


def send_message(receiver_type, product_name, percentage, users_collection):
    for user in users_collection.find():
        if user.get("type") == receiver_type:
            body = write_message(receiver_type, user.get("name"), product_name, percentage)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(SENDER, MAIL_PASSWORD)

            body_html = MIMEText(body, 'html')
            message = MIMEMultipart("alternatives")
            message['From'] = SENDER
            message['Subject'] = 'New at RetailX!'
            message['To'] = user.get("email")
            message.attach(body_html)
            s.sendmail(SENDER, user.get("email"), message.as_string())
            print("haidaaa")
            s.quit()


#send_message("customer", "basketball shoes", "15")

#write_message("customer", "Vlad", "basketball shoes", "20")

