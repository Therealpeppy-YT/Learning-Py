# Example Lines of code are indented once but still commented
# Variable = a container dor a value. Behaves as the value that it contains. Like algebra where you solve for x then you can reuse the new "x = __" value


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

# If you want to combine strings and ints in a print statement you have to do something called "Type casting"
# you can type cast by surrounding the variable name with parentheses and adding str before them with no space ex:
#   print("Your account is: "+ str(accountAge)+" years old.")