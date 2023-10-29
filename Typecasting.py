# ---------- Type casting ----------

# Type casting is the means of converting the data type of a value to another one

# In this example we have 3 values x, y, and z which happen to be of different data types
# x happens to be a Integer, y is a float, and z is a String

#   x = 1 -- Integer
#   y = 2.0 -- Float
#   z = "3" -- Str


# If we print these as is they will show up as

# 1
# 2.0
# 3

# but if we need y to be an integer you need to type cast. To type cast you need ti surround your variable with parentheses and precede them with the variable type you need to change it to
# in this case we need to change the variable y to and integer so instead of print(y) you would type print(int(y))
# this change is not permanet and only lasts for the one print statement if you need it to last for the entire peice of code you need to write [variable name] = variableyouneedtochangeto([ariablenameagain])
# so for this example you would write y = int(y) before your print statments
# after these changes when you run it again it will return

# 1
# 2
# 3

# BUT z is still a string which you CANNOT do math on so we need to type cast it too (if you try to do math on a string it will just rewrite it multiple times ex: print(z) will return 333)
# now we need to do the same thing for z so you can either make a temparary change and wrtie print(int(z)) or you can make a permanant change and write z = int(z) before your print statments

# Now you can repeat this procces with the the other variable types so you can change it to floats by typing
# x = float(x)
# y = float(y)
# z = float(z)
# and when run will return

# 1.0
# 2.0
# 3.0