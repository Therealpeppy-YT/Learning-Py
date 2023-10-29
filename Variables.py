# Example Lines of code are indented once but still commented
# Variable --- Values are containers for values. They behave as the value that they contains. Like algebra where you solve for x then you can reuse the new "x = __" value


# You can check the type of a variable by putting "print(type([name of variable]))" ex:
#    Checkme = "Im a string!"
#    print(type(Checkme))


# ---------- Strings aka str - Strings are a series of characters surrounded buy single quotes '' or double quotes "" ---------- 


#   username = "Therealpeppy"
#   password = "123456789"
#   full_userpass = username+" "+password
# when printing variables you don't put the variable name in quotes as that will print the NAME of the variable and not the VALUE of the variable.
# when printing variables with a string value you can also combine them with other stings ex:
#   print("Hello"+username)
#   print("Your User & Pass is: "+full_userpass+", Is this correct?")

# ---------- Ints - Ints or Integers are full numbers NOT surrounded by quotes '' nor double quotes "" ---------- 

# The following lines define the integer variable named accountAge is equivalent to 3 then it redifines it saying the accountAge is equivelent to accountAge (3) + 1 so when you print accountAge the console will show 4
    #accountAge = 3
    #accountAge = accountAge + 1
    #print(accountAge)

# But there is a shorter way of writing this, instead of saying "accountAge = accountAge + 1" you can instead write
    #accountAge += 1

# To learn how to print strings in combination with other variable types go to Typecasting.py

# ---------- Floats - Floats aka Floating Point Number (a decimal) are is a number value with a decimal NOT surrounded by quotes '' nor double quotes "" ---------- 

# The following line is an example of a Float.
#   userHeight = 5.4
# Yet again if you wanted to combine it with a string in a print statement you would need to Type cast -- Line 31
#   print("Therealpeppy's height is: "+str(userHeight)+"ft")

# ---------- Boolean - Booleans aka bools are just simple True or False variable ---------- 

# When typing bools make sure to capitalize the T and F

# The following line is an example of a Bool.
#   good_at_coding = false
# Lastly if you wanted to combine them with strings in a print statement you would have to do the same as before -- Line 31
#   print("Are you good at coding: "+str(good_at_coding))




# Multiple assignment --- Multiple assignment allows us to assign multiple variables at the same time in one line of code

# The following lines are an example of Standard assignment
#   userName = "Therealpeppy"
#   accountAge = 3
#   cool = True  

# Now we are going to do the same but use Multiple assignment
#   userName, accountAge, cool = "Therealpeppy", 3, True

# As you see when using multiple assignment you need to seperate all the Names for the variables with commas, and you need to separate the values with commas too
# you also need to list the values in the same order as the names or else all of your variables will be mismatched

# If your variables are all equal to the same thing there is slightly different procedure ex:
#   user1Age = user2Age = user3Age = 23



