# import pandas as pd
# from scipy.stats import zscore
# import matplotlib.pyplot as plt
# from io import StringIO
#
# # Datele tale sub formă de șir
# data_str = """Product_ID	Date	Sales	Revenue	EndOfDayStock
# 16048	2009-12-08	24	10.08	2192
# 16048	2009-12-13	1	0.42	2191
# 16048	2009-12-14	2	0.84	2189
# 16048	2009-12-18	24	10.08	2165
# 16048	2010-01-08	24	10.08	2141
# 16048	2010-01-10	480	57.6	1661
# 16048	2010-01-18	96	11.52	1565
# 16048	2010-02-24	24	10.08	1541
# 16048	2010-03-04	120	21.6	1421
# 16048	2010-04-08	1	0.42	1420
# 16048	2010-04-14	96	11.52	1324
# 16048	2010-05-24	120	21.6	1204
# 16048	2010-06-30	24	10.08	1180
# 16048	2010-07-08	4	1.68	1176
# 16048	2010-07-12	1	0.42	1175
# 16048	2010-08-03	24	10.08	1151
# 16048	2010-08-22	24	10.08	1127
# 16048	2010-09-27	768	92.16	359
# 16048	2010-10-01	24	10.08	335
# 16048	2010-11-18	96	11.52	239
# 16048	2010-12-16	24	10.08	215
# 16048	2011-03-28	96	11.52	119
# 16048	2011-03-31	96	11.52	23
# 16048	2011-04-27	96	11.52	24
# 16048	2011-05-08	24	10.08	0
# 16048	2011-06-05	24	2.88	144
# 16048	2011-06-16	144	17.28	0
# 16048	2011-06-19	24	2.88	96
# 16048	2011-06-27	96	11.52	0
# 16048	2011-07-06	24	2.88	48
# 16048	2011-07-14	48	5.76	0
# 16048	2011-07-17	24	2.88	24
# 16048	2011-07-18	24	2.88	0
# 16048	2011-07-31	24	2.88	48
# 16048	2011-08-11	48	5.76	0
# 16048	2011-08-15	24	2.88	24
# 16048	2011-08-16	24	2.88	0
# 16048	2011-08-18	24	2.88	24
# 16048	2011-08-25	24	2.88	0
# 16048	2011-08-26	24	2.88	24
# 16048	2011-08-31	24	2.88	0
# 16048	2011-09-05	48	5.76	24
# 16048	2011-09-09	24	2.88	0
# 16048	2011-09-27	48	5.76	24
# 16048	2011-09-29	24	2.88	0
# 16048	2011-10-05	24	2.88	7
# 16048	2011-10-09	7	0.84	0
# 16048	2011-10-10	48	5.76	24
# 16048	2011-10-17	24	2.88	0
# 16048	2011-10-19	10	1.2	25
# 16048	2011-10-20	25	3	0
# 16048	2011-10-30	72	8.64	24
# 16048	2011-11-01	24	2.88	0
# 16048	2011-11-03	24	2.88	24
# 16048	2011-11-14	24	2.88	0
# 16048	2011-11-15	2	0.24	1
# 16048	2011-11-18	1	0.12	0
# 16048	2011-11-22	24	2.88	24
# 16048	2011-11-25	24	2.88	0
# """
#
# # Transformă datele într-un obiect DataFrame
# data = pd.read_csv(StringIO(data_str), sep='\s+')
#
# # Specifică Product_ID-ul pentru care vrei să identifici anomaliile
# product_id_to_analyze = 16048
#
# # Filtrăm datele pentru Product_ID-ul specificat
# selected_data = data[data['Product_ID'] == product_id_to_analyze]
#
# # Calculăm Z-Score pentru coloana 'EndOfDayStock'
# selected_data['Z_Score'] = zscore(selected_data['EndOfDayStock'])
#
# # Setăm un prag pentru a identifica anomaliile Z-Score (de exemplu, Z-Score mai mic de -2 sau mai mare de 2)
# z_score_anomaly_threshold = 2
# z_score_anomalies = selected_data[(selected_data['Z_Score'] < -z_score_anomaly_threshold) | (selected_data['Z_Score'] > z_score_anomaly_threshold)]
#
# # Setăm pragul pentru a identifica stocul epuizat (valoarea 0)
# zero_stock_anomalies = selected_data[selected_data['EndOfDayStock'] == 0]
#
# # Setăm un prag pentru a identifica stocul foarte mic (pragul poate fi ajustat în funcție de nevoi)
# low_stock_threshold = 5  # Exemplu: pragul este setat la 5, dar poate fi modificat
# low_stock_anomalies = selected_data[(selected_data['EndOfDayStock'] < low_stock_threshold) & (selected_data['EndOfDayStock'] != 0)]
#
# # Afișăm graficul cu valorile istorice ale stocurilor și marcăm anomaliile
# plt.figure(figsize=(10, 6))
# plt.plot(selected_data['Date'], selected_data['EndOfDayStock'], label='EndOfDayStock')
# plt.scatter(z_score_anomalies['Date'], z_score_anomalies['EndOfDayStock'], color='red', label='Anomalii Z-Score')
# plt.scatter(zero_stock_anomalies['Date'], zero_stock_anomalies['EndOfDayStock'], color='orange', label='Stoc Epuizat')
# plt.scatter(low_stock_anomalies['Date'], low_stock_anomalies['EndOfDayStock'], color='purple', label='Stoc Foarte Mic')
# plt.xticks(rotation=45)
# plt.xlabel('Date')
# plt.ylabel('EndOfDayStock')
# plt.title(f'Anomalii în valorile istorice ale stocurilor pentru Product_ID {product_id_to_analyze}')
# plt.legend()
# plt.show()
#
# # Afișăm tabelul cu datele, Z-Score și detecția de stoc epuizat și stoc foarte mic
# print(selected_data[['Date', 'EndOfDayStock', 'Z_Score']])
# print('\nAnomalii Z-Score:')
# print(z_score_anomalies[['Date', 'EndOfDayStock', 'Z_Score']])
# print('\nStoc Epuizat:')
# print(zero_stock_anomalies[['Date', 'EndOfDayStock']])
# print('\nStoc Foarte Mic:')
# print(low_stock_anomalies[['Date', 'EndOfDayStock']])
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Citirea datelor din fișierul Excel
file_path = "sales_and_eodStocks.xlsx"
data = pd.read_excel(file_path)

# Specifică Product_ID-ul pentru care vrei să identifici anomaliile
product_id_to_analyze = 16048

# Filtrăm datele pentru Product_ID-ul specificat
selected_data = data[data['Product_ID'] == product_id_to_analyze]

# Calculăm Z-Score pentru coloana 'EndOfDayStock'
selected_data['Z_Score'] = zscore(selected_data['EndOfDayStock'])

# Setăm un prag pentru a identifica anomaliile Z-Score (de exemplu, Z-Score mai mic de -2 sau mai mare de 2)
z_score_anomaly_threshold = 2
z_score_anomalies = selected_data[(selected_data['Z_Score'] < -z_score_anomaly_threshold) | (selected_data['Z_Score'] > z_score_anomaly_threshold)]

# Setăm pragul pentru a identifica stocul epuizat (valoarea 0)
zero_stock_anomalies = selected_data[selected_data['EndOfDayStock'] == 0]

# Setăm un prag pentru a identifica stocul foarte mic (pragul poate fi ajustat în funcție de nevoi)
low_stock_threshold = 5  # Exemplu: pragul este setat la 5, dar poate fi modificat
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
plt.show()

# Afișăm tabelul cu datele, Z-Score și detecția de stoc epuizat și stoc foarte mic
print(selected_data[['Date', 'EndOfDayStock', 'Z_Score']])
print('\nSupra-stoc:')
print(z_score_anomalies[['Date', 'EndOfDayStock', 'Z_Score']])
print('\nStoc Epuizat:')
print(zero_stock_anomalies[['Date', 'EndOfDayStock']])
print('\nStoc Foarte Mic:')
print(low_stock_anomalies[['Date', 'EndOfDayStock']])
