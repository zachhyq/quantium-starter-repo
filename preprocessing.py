import pandas as pd

d1 = pd.read_csv('data/daily_sales_data_0.csv')
d2 = pd.read_csv('data/daily_sales_data_1.csv')
d3 = pd.read_csv('data/daily_sales_data_2.csv')

#1. Drop the non (pink morsel) products
d1 = d1[d1['product'] == "pink morsel"]
d2 = d2[d2['product'] == "pink morsel"]
d3 = d3[d3['product'] == "pink morsel"]

#2. Combine quantity and price into sales
d1['sales'] = d1['price'].str.replace('$', '').astype(float) * d1['quantity']
d2['sales'] = d2['price'].str.replace('$', '').astype(float) * d2['quantity']
d3['sales'] = d3['price'].str.replace('$', '').astype(float) * d3['quantity']


#3 drop the unnecessary columns
d1 = d1.drop(columns=['product','price', 'quantity'])
d2 = d2.drop(columns=['product','price', 'quantity'])
d3 = d3.drop(columns=['product','price', 'quantity'])

#4 merge into a single dataframe then export it
dfres = pd.concat([d1,d2,d3])
dfres = dfres[['sales', 'date', 'region']]
dfres.to_csv('data/processed_data.csv', index=False)




