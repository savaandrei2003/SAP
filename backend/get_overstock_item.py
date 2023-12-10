from datetime import datetime
import pandas as pd

file_path = "sales_and_eodStocks.xlsx"
data = pd.read_excel(file_path)
transactions_document = pd.read_excel("transactions_og.xlsx")

last_day = datetime.strptime("2009-11-01", "%Y-%m-%d")
eod_stock = 0
product_id = 1

for index, row in data.iterrows():
    try:
        date = datetime.strptime(str(row["Date"]), "%Y-%m-%d %H:%M:%S")
        if date > last_day:
            eod_stock = row["EndOfDayStock"]
            product_id = row["Product_ID"]
            last_day = date
        elif date == last_day and eod_stock < row["EndOfDayStock"]:
            eod_stock = row["EndOfDayStock"]
            product_id = row["Product_ID"]
    except Exception as e:
        print(e)


description = ""

for index, row in transactions_document.iterrows():
    if row["Product_ID"] == product_id:
        description = row["Description"]
        break

print(description)
print(eod_stock)
