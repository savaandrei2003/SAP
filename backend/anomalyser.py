import json
import base64

import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Citirea datelor din fișierul Excel
file_path = "sales_and_eodStocks.xlsx"
data = pd.read_excel(file_path)


def retrieve_anomalies(product_id_to_analyze):
    selected_data = data[data['Product_ID'] == product_id_to_analyze]

    # Calculăm Z-Score pentru coloana 'EndOfDayStock'
    selected_data['Z_Score'] = zscore(selected_data['EndOfDayStock'])

    # Setăm un prag pentru a identifica anomaliile Z-Score (de exemplu, Z-Score mai mic de -2 sau mai mare de 2)
    z_score_anomaly_threshold = 2
    z_score_anomalies = selected_data[(selected_data['Z_Score'] < -z_score_anomaly_threshold) | (selected_data['Z_Score'] > z_score_anomaly_threshold)]

    # Setăm pragul pentru a identifica stocul epuizat (valoarea 0)
    zero_stock_anomalies = selected_data[selected_data['EndOfDayStock'] == 0]

    # Setăm un prag pentru a identifica stocul foarte mic (pragul poate fi ajustat în funcție de nevoi)
    low_stock_threshold = 30  # Exemplu: pragul este setat la 5, dar poate fi modificat
    low_stock_anomalies = selected_data[(selected_data['EndOfDayStock'] < low_stock_threshold) & (selected_data['EndOfDayStock'] != 0)]

    # Afișăm graficul cu valorile istorice ale stocurilor și marcăm anomaliile
    plt.figure(figsize=(10, 6))
    plt.plot(selected_data['Date'], selected_data['EndOfDayStock'], label='EndOfDayStock')
    plt.scatter(z_score_anomalies['Date'], z_score_anomalies['EndOfDayStock'], color='red', label='Anomalii Z-Score')
    plt.scatter(zero_stock_anomalies['Date'], zero_stock_anomalies['EndOfDayStock'], color='orange', label='Stoc Epuizat')
    plt.scatter(low_stock_anomalies['Date'], low_stock_anomalies['EndOfDayStock'], color='purple', label='Stoc Foarte Mic')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('EndOfDayStock')
    plt.title(f'Anomalii în valorile istorice ale stocurilor pentru Product_ID {product_id_to_analyze}')
    plt.legend()
    plt.savefig("stats.png")
    plt.show()

    with open('stats.png', 'rb') as image_file:
        image_binary_data = image_file.read()

    photo = base64.b64encode(image_binary_data).decode("utf-8")
    return {"photo": photo}

