import pandas as pd


#here df.shape give the no of rows and coloumns
'''
df =pd.read_csv("test.txt")
print(df.shape)
'''

"""we had already imported pandas now we are going to learn about Data Frame
NOW remeber we can name a varaible for a file it doesnt need to be always df
we can also put the table inside DataFrame without makin a variable called data"""

data={"name":["a","b","c","d"],"age":[2,3,4,5],"city":["tokyo","ital","lowerit","boll"]}
table=pd.DataFrame(data)
print(table.shape)
print(table.isnull)