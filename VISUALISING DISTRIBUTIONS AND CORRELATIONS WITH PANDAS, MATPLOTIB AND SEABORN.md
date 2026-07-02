# INTRODUCTION TO DATA VISUALIZATION

It is the process of reprsenting data using groaphs and charts so we can understand it easily instead of reading thousands of numbers

it hep us in ==find patterns== ==detect outliers== ==understand distribution== ==find relationships==

# MAINLY WE USE 3 LIBRARIES

# 1.PANDAS
Used to ==load and manage data== 

![[Pasted image 20260630020852.png]]

# 2.MATPLOTLIB

used to create==graph== 
![[Pasted image 20260630020948.png]]

# 3.SEABORN

built on top of matploib

![[Pasted image 20260630021053.png]]
 it creates more attractive ==statistical plots with less code== 

![[Pasted image 20260630185311.png]]

![[Pasted image 20260630021105.png]]

# TYPES OF VISUALISATION

# 1.UNIVARIATE PLOT
uni =one

only one variable is analyzed

eg: ==HISTOGRAM== , ==BOX PLOT==

# 2.BIVARIATE PLOT

Two variable

eg: ==scatter plot


![[Pasted image 20260630190307.png]]

![[Pasted image 20260630190330.png]]

# note
DISTRIBUTION MEANS HOW THE VALUES ARE SPREAD ACROSS THE DATASET

![[Pasted image 20260630190458.png]]

# BINS ARE LIKE RANGES OF DATA
![[Pasted image 20260630190534.png]]
![[Pasted image 20260630190545.png]]

# ==CREATING A HISTOGRAM IN PANDAS

[[PANDAS]] ==refer here to get more details==



import pandas as pd

data={"age":[18,20,19,22,18,21,20,19,22,23]}

df=pd.DataFrame(data)

df["age"].hist()

not proper


# ==CREATING A HISTOGRAM IN MATPLOTLIB==

[[MATPLOTLIB]]

![[Pasted image 20260630200744.png]]
![[Pasted image 20260630200758.png]]

# WE CAN CHANGE THE NO OF BINS
DEFAULT BINS ARE USUALLY 10

SYNTAX TO CHANGE: ==plt.hist(df["age"], bins=5)== 
![[Pasted image 20260630201118.png]]

![[Pasted image 20260630201200.png]]

# WE CAN LABEL X AXIS AND Y AXIS AND GIVE A TITLE
![[Pasted image 20260630201744.png]]

![[Pasted image 20260630201815.png]]
![[Pasted image 20260630201830.png]]![[Pasted image 20260630201846.png]]


# BOX PLOT

![[Pasted image 20260630201944.png]]![[Pasted image 20260630203221.png]]
![[Pasted image 20260630221845.png]]

[[SEABORN]]

 ![[Pasted image 20260630225102.png]]
 ![[Pasted image 20260630225023.png]]

![[Pasted image 20260630225316.png]]

# SCATTER PLOT
![[Pasted image 20260630230215.png]]
![[Pasted image 20260630230229.png]]

![[Pasted image 20260630230249.png]]
![[Pasted image 20260630230326.png]]
![[Pasted image 20260630230341.png]]
# CREATING A SCATTER PLOT

# USING METPLOTLIP

![[Pasted image 20260630230522.png]]

# USING SEABORN

![[Pasted image 20260630230606.png]]

# ALWAYS REMEBER ==WE CAN LABEL THESE GRAPHS WITH FOLOWING==

![[Pasted image 20260630230853.png]]

# CORRELATION

CORRELATION TELLS US 
How strongly two variables are related

![[Pasted image 20260630231329.png]]![[Pasted image 20260630231341.png]]
![[Pasted image 20260630231404.png]]

# in positive correlation both variables increase together

# in negative correlation one increase and other decreases

# in zero correlation no relationship


# ==CORRELATION COEFFICIENT==

REPRESENTED BY ' r '

![[Pasted image 20260630231730.png]]
![[Pasted image 20260630231744.png]]

# correlation pandas

![[Pasted image 20260630231819.png]] 

![[Pasted image 20260630231915.png]]

![[Pasted image 20260630235941.png]]
![[Pasted image 20260630235954.png]]


# HEAT MAP

![[Pasted image 20260701000145.png]]

![[Pasted image 20260701000219.png]]
![[Pasted image 20260701000252.png]]

![[Pasted image 20260701000413.png]]![[Pasted image 20260701000432.png]]
![[Pasted image 20260701000637.png]]


![[Pasted image 20260701000616.png]]

![[Pasted image 20260701000702.png]]