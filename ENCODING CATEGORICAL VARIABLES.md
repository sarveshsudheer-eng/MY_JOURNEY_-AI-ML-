____
![[Pasted image 20260627183415.png]]![[Pasted image 20260627183447.png]]
Most ml algorithms require numberical inputs 

so we must conver the text into numbers
this conversion is called ===enccoding===

choosing the correct encoding method the machine learning model can understand the data correctly 

# types of categorical data

# 1. Nominal data:
consists of categories without any ===inherent order or ranking===

example : 'red', 'blue', 'green' (car color)

encoding optionns: ===one- hot encoding or label encoding === depending on the models needs

# 2. Ordinal data:

includes categoreis with a ==defined order or ranking==  where the relationship between values is important

example : 'low' , 'mediujm' , 'high' (car engine power )

encoding options: ==Ordinal encoding==

# for labeled encoding and other encoding pls look geeksforgeeks and study

we will only concentrate on ==one hot and ordinal encoding== 

# 1. ONE-HOT ENCODING
#onehotencoding

It is actually used when the data **is categorical** (text categories), ==but those categories do not have any natural order.== 

and here we use ==table like representation with binary input each coloumn is a feature and for each input we will put 1 in case if the given data is of that category and all other 0== 

 ![[Pasted image 20260627185437.png]]
# syntax for one hot encoding is

==pd.get_dummies(df)== 
 ![[Pasted image 20260627220106.png|341]]
can also be ==represented as == 
![[Pasted image 20260627220547.png]]

# ORDINAL ENCODING

Ordinal Encoding maps ==categories to integers while preserving their natural order==


- Categories ➜ converted to numbers.
- The numbers are chosen so they **follow the original ranking**.
![[Pasted image 20260627223417.png]]![[Pasted image 20260627223436.png]]![[Pasted image 20260627223446.png]]



# NOTE ==VERY IMP== 

==In Python, **single quotes (`' '`) and double quotes (`" "`) are exactly the same** for defining strings.==

![[Pasted image 20260627224422.png]]