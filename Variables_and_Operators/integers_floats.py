#%%
# Lets look at some other data types
# integers, or ints, are whole numbers, from -2147483648 to 2147483647
# lets store an integer

a = 0

#%%
# Because python is type-inferred, we do not specify the data type of the variable
# instead, we give the variable the data we want, and python determines its type
# We can see the type of the variable in the variables pane in Python Interactive
# You can also use the type() function to determine the type

print(type(a))

# Notice that this prints out <class 'int'>. That is because python is an object
# oriented language, so all data types are defined in classes. We will look more
# at objects later.
#%%
# floats are for decimal numbers and fractions
f = 3.2
# this has type float, and a value of 3.2
#%%
# what happens if we try 0.0?
g = 0.0
# g is a float, even though it is the same mathematically as 0
# %%
# Lets try some user input
in_int = input("Enter an integer")
# check its type in Python Interactive
# Its a string! The same way 0.0 is a float and 0 is an int, "0" is a string
#%%
# what if we don't want it to be a string? we use the casting functions.
int("1") # Turns any type into its equivalent integer value
float("1") # Turns any type into its equivalent float value
str(1) # Turns any type into its equivalent string value
# %%
# now lets try getting an int input again
# YOUR CODE BELOW

