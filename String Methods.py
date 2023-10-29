# ---------- String Methods ----------

# String methods are different adjectives you can add to your variables in your print statments to "describe" them.
# For these examples I will be using the variable
#   userName = Therealpeppy

# The first string method is the len aka length string method
# The len string method prints the total amount of characters in the string to the console. (Spaces are characters)
# For example print(len(userName)) would return 12 to the console

# The next string method is the find string method
# The find string method prints out where in the string a certain character is. 
# For example print(userName.find("T")) would return 0 to the console.  (Computer start counting at 0 so if the letter/character is at the start it will return 0)

# The next few string methods are quite self explanitory but I will still tell you what they do
#   print(userName.capitalize()) will capitalize the first letter in your string (does not extend past spaces)
#   print(userName.upper()) will make your entire string UPPERCASE (Does extend past spaces)
#   print(userName.lower()) will make your entire string LOWERCASE (Does extend past spaces)
#   print(userName.isdigit()) will return a True or False statment depending on if your string is entirely numbers aka 123 or not
#   print(userName.isalpaha()) will return a True or False statment depending on if your string is entirely alphabetic aka abc or not (characters like spaces and !?!@#$ etc do not count as alphabetic and if they are in your string it will return as False)
#   print(userName.replace("e", "o")) will replace all the e's with o's. Returning Thoroalpoppy


# The string method count essentialy does the same as the len string method but for a single character (formatted same as find just replaced with count)
# For example print(userNamel.count("e")) would return 3 as there are 3 e's in the string variable userName -- line 76
