import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Citirea datelor din fișierul Excel
file_path = "sales_and_eodStocks.xlsx"
data = pd.read_excel(file_path)

# Specifică Product_ID-ul pentru care vrei să faci predicții
product_id_to_predict = 16048

# Filtrăm datele pentru Product_ID-ul specificat
selected_data = data[data['Product_ID'] == product_id_to_predict]

# Selecția de caracteristici (X) și variabila de răspuns (y)
X = selected_data[['Sales']]
y = selected_data['EndOfDayStock']

# Aplicăm transformarea polinomială
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Inițializarea modelului de regresie liniară
model = LinearRegression()

# Antrenarea modelului
model.fit(X_poly, y)

# Introducerea datei de la tastatură
input_date_str = input("Introduceti data (YYYY-MMMM-DDDD): ")

# Convertirea datei introduse într-un obiect datetime
input_date = pd.to_datetime(input_date_str)

# Transformarea datei într-un array 2D pentru a putea fi folosită în modelul nostru
input_date_array = np.array([[input_date.day]])

# Aplicăm transformarea polinomială pe data introdusă
input_date_poly = poly.transform(input_date_array)

# Realizăm predicția pentru data introdusă
predicted_stock = model.predict(input_date_poly)

# Afișarea rezultatului
print(f'Predicția pentru data {input_date_str}: {int(predicted_stock[0])}')
