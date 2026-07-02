import pandas as pd

data = {"color":['Red', 'Blue', 'Green', 'Red']}

df = pd.DataFrame(data)
one_hot_encoded = pd.get_dummies(df)

print(one_hot_encoded)