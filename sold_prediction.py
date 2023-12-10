import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Citirea datelor din fișierul Excel
file_path = "sales_and_eodStocks.xlsx"
data = pd.read_excel(file_path)

# Introducerea Product_ID-ului de la tastatură
product_id_to_predict = int(input("Introduceti Product_ID-ul pentru care vreti sa faceti predictia: "))

# Filtrarea datelor pentru Product_ID-ul specificat
selected_data = data[data['Product_ID'] == product_id_to_predict]

# Selecția de caracteristici (X) și variabila de răspuns (y)
X = selected_data[['Sales']]
y = selected_data['EndOfDayStock']

# Aplicarea transformării polinomiale
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
X_poly = poly.fit_transform(X)

# Obținerea numelor caracteristicilor într-un mod personalizat
feature_names = [f'Sales^({i})' for i in range(1, degree + 1)]
X_poly_df = pd.DataFrame(X_poly, columns=feature_names)

# Inițializarea modelului de regresie liniară
model = LinearRegression()

# Antrenarea modelului
model.fit(X_poly_df, y)

# Introducerea datei de la tastatură
input_date_str = input("Introduceti data (YYYY-MMMM-DDDD): ")

# Convertirea datei introduse într-un obiect datetime
input_date = pd.to_datetime(input_date_str)

# Transformarea datei într-un array 2D pentru a putea fi folosită în modelul nostru
input_date_array = np.array([[input_date.day]])

# Aplicarea transformării polinomiale pe data introdusă
input_date_poly = poly.transform(input_date_array)

# Realizarea predicției pentru data introdusă
predicted_stock = model.predict(input_date_poly)

# Estimarea timpului până la terminarea stocului
days_until_zero_stock = int(model.intercept_ / model.coef_[0])

# Afișarea rezultatului
print(f'Predicția pentru data {input_date_str}: {int(predicted_stock[0])} unități de stoc.\n'
      f'Estimare: Stocul se va termina în aproximativ {days_until_zero_stock} zile.')
