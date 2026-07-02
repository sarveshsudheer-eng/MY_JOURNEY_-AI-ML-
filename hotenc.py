import pandas as pd

data={"coloumn":["red","blue","green","red","green"]}

df=pd.DataFrame(data)
hot_encoder= pd.get_dummies(df)
print(hot_encoder)