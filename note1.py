import pandas as pd
import numpy as np
df=pd.DataFrame({"name":[pd.NA,"B","C"],"age":[2,np.nan,5],"city":["a","b","c"],"happy":["YES",None,"YES"]})
print(df.dropna())
