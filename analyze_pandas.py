import pandas as pd

df = pd.read_csv('World_Airports.csv', header=0, na_values=[])
# print(df.head()) # print first 5 rows
# print(df.tail()) # print first 5 rows
# print(df[['id', 'airport_ident']]) # print only id and airport_ident columns

# Iterate over rows and print id and airport_ident
# for index, row in df.iterrows(): 
#     print(row['id'], row['airport_ident'])  

# Iterate over rows and print name and iso_country
# for index, row in df.iterrows():
#     print(row['name'], row['iso_country'])

# print only rows with name = "Goldstone (GTS) Airport"
print(df.loc[df['name']=="Goldstone (GTS) Airport"])