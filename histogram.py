import pandas as pd
import matplotlib.pyplot as plt

data={"age":[18,20,19,22,18,21,20,19,22,23]}

df=pd.DataFrame(data)
plt.hist(df, bins=5
         )
plt.show()

