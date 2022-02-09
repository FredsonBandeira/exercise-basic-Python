import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df
