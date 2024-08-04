import json
import pandas as pd


file = open('dados/vendas.json')
data = json.load(file)

# print(data)

df = pd.DataFrame.from_dict(data)

#print(df['Data da Compra'])

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()

