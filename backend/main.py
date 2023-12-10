from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import json
import anomalyser
import sold_prediction
import send_targeted_message
import send_general_message
from pymongo import MongoClient
from datetime import datetime


app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'sunt-smecher'
os.environ["OPENAI_API_KEY"] = ""

client = MongoClient("mongodb+srv://ionescupv:UglY1rwP9Olt1mSH@cluster0.sdirhd9.mongodb.net/")
db = client.get_database("sap")
users_collection = db.get_collection("users")


@app.route("/products", methods=["POST"])
@cross_origin()
def get_stock_evolution():
    frontend_input = request.get_json()["product_id"]
    print(frontend_input)
    return json.dumps(anomalyser.retrieve_anomalies(frontend_input))


@app.route("/product-prediction", methods=["POST"])
@cross_origin()
def get_product_prediction():
    product_id = request.get_json()["product_id"]
    date = request.get_json()["date"]
    input_date = datetime.strptime(date, "%a %b %d %Y %H:%M:%S GMT%z")
    formatted_date = input_date.strftime("%Y-%m-%d %H:%M:%S")
    prediction = sold_prediction.get_prediction(product_id, formatted_date)
    return prediction


@app.route("/targeted-message", methods=["POST"])
@cross_origin()
def send_targeted_message_to_costumer():
    send_targeted_message.send_targeted_message(users_collection=users_collection)
    return {"status": "success"}


@app.route("/general-message-to-costumer", methods=["POST"])
@cross_origin()
def send_general_message_to_customer():
    product_name = request.get_json()["product"]
    percentage = request.get_json()["percentage"]
    send_general_message.send_message("customer", product_name, percentage, users_collection)
    return {"status": "success"}


@app.route("/general-message-to-employee", methods=["POST"])
@cross_origin()
def send_general_message_to_employee ():
    product_name = request.get_json()["product"]
    percentage = request.get_json()["percentage"]
    send_general_message.send_message("employee", product_name, percentage, users_collection)
    return {"status": "success"}


if __name__ == "__main__":
    app.run(debug=True)
