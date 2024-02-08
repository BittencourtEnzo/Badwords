
import pandas

import csv
with open('ibge-mas-10000.csv', 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    print(reader[0][0])