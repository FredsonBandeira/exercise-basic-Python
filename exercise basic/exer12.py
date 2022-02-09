df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

df.to_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
