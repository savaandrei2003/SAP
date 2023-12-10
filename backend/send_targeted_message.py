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


def send_targeted_message(users_collection):
    prompts = {"14191": "The user with id 14191 bought cake stand white two tier lace, cake stand lovebird 2 tier pink, hairclips forties fabric assorted, danish rose decorative plate, danish rose round sewing box, danish rose trinket trays, danish rose deluxe coaster, bicycle puncture repair kit , lunch bag paisley park  , vintage doily jumbo bag red , jumbo bag alphabet, jumbo bag paisley park, charlotte bag pink polkadot, red retrospot charlotte bag, lunch bag red retrospot and fairy cake flannel assorted colour from our webstore. What should he buy next? Write the response as a kind advertisement to the customer. The name of the company is RetailX. Make the message short and friendly.", "16794": "The user with id 16794 bought recipe box pantry yellow design, set of 6 herb tins sketchbook, recipe box pantry yellow design, set of 3 cake tins sketchbook, skull design tv dinner tray, set 3 retrospot tea,coffee,sugar and set of 3 cake tins pantry design from our webstore. What should he buy next? Write the response as a kind advertisement to the customer. The name of the company is RetailX. Make the message short and friendly."}

    for key, value in prompts.items():
        filter_criteria = {"id": key}
        user = users_collection.find_one(filter=filter_criteria)
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": value}],
            "temperature": 0.7
        }
        generated_text = requests.post(url=API_PATH, headers=headers, data=json.dumps(payload))
        body = generated_text.json()["choices"][0]["message"]["content"]
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
