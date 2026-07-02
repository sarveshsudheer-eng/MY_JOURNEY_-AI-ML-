 
![[Pasted image 20260627105445.png]]![[Pasted image 20260627105502.png]]![[Pasted image 20260627105512.png]]![[Pasted image 20260627105529.png]]


# Before going in some points to remember in python DATA FRAME
----
#DATAFRAME

Data frame is a 2 d table in python by the pandas library

We can use it to make tables  
Now the syntax is :

                                        Table=pd.DataFrame({“Name”:[“A”, “B”, “C”], “Age”:[12, 34, 67], “City”:[“a”, “b”, “c”]})

  
Here the whole table is in { } and each coloumn name is put with “” and then : and []

Inside [] u type the data in each of the coloumn corresponding to it like A,B,C,a,b,……….  
  

Other way to use DataFrame is to put the table in a variable and put that variable inside the DataFrame

                                        Data={“Name”:[“A”, “B”, “C”], “Age”:[12,34,67], “City”:[“a”, “b”, “c”]}  
                                        Table=pd.DataFrame(Data)
                                        
 
  ![[Pasted image 20260627105931.png]]   

# Now lets make a null values here
 #NULLVALUES
for adding null variables either u can do like “none” in place of string
![[Pasted image 20260627110532.png]]for numerical values we can import numpy and put np.nan![[Pasted image 20260627110551.png]]![[Pasted image 20260627110600.png|214]]

For panda coloumn we can use ==pd.NA==

![[Pasted image 20260627110647.png|276]]
NOW LETS ADD ALL THESE IN A SINGLE![[Pasted image 20260627110757.png]]![[Pasted image 20260627110803.png]]

# GO THROUGH GIVEN LINK FOR LEARNING ABOUT NUMPY 
 #NUMPY
 
[[NUMPY]]
AFTER GOING THROUGH NUMPY LETS COME BACK

Now we are going to look certain functions used to handle ==null values==

# ==IMP==
![[Pasted image 20260627143834.png]]

# ISNULL
#ISNULL
![[Pasted image 20260627114314.png]]
![[Pasted image 20260627115100.png]]![[Pasted image 20260627115104.png]]

![[Pasted image 20260627114436.png]]
![[Pasted image 20260627114454.png]]

# NOTNULL
#notnull

both are almost same
![[Pasted image 20260627115235.png]]
# ISNA

isna same as isnull

# DROPNA
#DROPNA
![[Pasted image 20260627140512.png]]

![[Pasted image 20260627140526.png]]

# FILLNA

#FILLNA
SYNTAX
df.fillna(value)


![[Pasted image 20260627140936.png]]![[Pasted image 20260627140952.png]]![[Pasted image 20260627141036.png]]![[Pasted image 20260627141115.png]]![[Pasted image 20260627141148.png]]
![[Pasted image 20260627141212.png]]

==for all the filling case it is important to do like 
redifine the variable as like df=df.fillna(value) or 
df.filllna(value, inplace=True)==
![[Pasted image 20260627141653.png]]

# REPLACE
#REPLACE
![[Pasted image 20260627142016.png]]
![[Pasted image 20260627142127.png|186]]![[Pasted image 20260627142147.png]]



![[Pasted image 20260627142219.png]]
![[Pasted image 20260627142241.png]]
SAME WE CAN DO FOR STRING

FOR MULTIPLE REPLACEMENT
![[Pasted image 20260627142344.png]]

# DUPLICATE

![[Pasted image 20260627142933.png]]

# UNIQUE

# COMPLETE THESE AREA



# IMPUTATION METHOD
#imputation


![[Pasted image 20260627144223.png]]![[Pasted image 20260627144432.png]]

# INTERPOLATION

![[Pasted image 20260627144601.png]]

