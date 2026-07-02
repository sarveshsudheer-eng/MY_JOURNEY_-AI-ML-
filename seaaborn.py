import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame({"marks":[2,3,4,5,5,5,4,3,2,4,6,7,4,23,]})

sns.boxplot(y=df["marks"])
plt.show()