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