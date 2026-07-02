from sklearn.preprocessing import OrdinalEncoder

data =[['low'],['high'],['medium'],['low'],['medium'],['high']]
encoder=OrdinalEncoder(categories=[['low','medium','high']])
encoded_data=encoder.fit_transform(data)
print(encoded_data)