An outlier is a data point that is very different from the rest of the data 

![[Pasted image 20260629221144.png]]![[Pasted image 20260629221158.png]]

# TYPES OF OUTLIERS

# 1. GLOBLA OUTLIER

a value that is far away from all other values
![[Pasted image 20260629221308.png]]

# 2.CONTEXTUAL OUTLIER

A group of values  together behaves unusually

eg: A sudden spike in network traffic over several minutes

# WHAT IS OUTLIER DETECTION

Outlier detection is the process of finding unusual or abnotmal data points in a dataset. its goal is to idnetify values that dont follow the general pattern


![[Pasted image 20260629225657.png]]

# COMMON METHODS OF OUTLIER DETECTION

# 1.Standar deviation method

if  data follows a noral distribuiton most values lie close to the mean

values that are more than about 2-3 standard deviation away from the mean are considered outliers

![[Pasted image 20260629231137.png]]

#series
[[PANDAS]] we are ==using series==
in below given example

![[Pasted image 20260629233539.png]]

![[Pasted image 20260629233559.png]]

now lets use ==datafreame==
![[Pasted image 20260629233835.png]]


# 2.IQR(interquartile range) method most ==iimp==


![[Pasted image 20260629234037.png]]

![[Pasted image 20260629234131.png]]

![[Pasted image 20260629235103.png]]
# 3. Z-Score Method

idea ==HOW MANY STANDARD DEVIATIONS A VALUE IS FROMM THE MEAN==

FORMULA

![[Pasted image 20260629234819.png]]
![[Pasted image 20260629234841.png|345]]

![[Pasted image 20260629235244.png]]



![[Pasted image 20260629234922.png]]
