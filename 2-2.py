
# myvar = "Say it ain't so"
# print(myvar)


# var2 = "Spam & Eggs"

# spam = "Spam"
# eggs = "Eggs"
# spam_and_eggs = spam + " & " + eggs

# print (var2[:])
# print (spam_and_eggs[:])
# length = len(spam_and_eggs)
# print(length)
# print(spam_and_eggs.upper())


# praise = "Good Doggie" #I declare a variable phrase with is a name and memory assigne to a string "good doggie"

# count = praise.upper().count("G") #declares a varriable count, name memroy and location of stored data, and assigning it to a value result from praise.upper().count("G")
# print("Count: ", count) #output from into displays info

# town = input("Enter the name of your City: ")
# fullName= input("Enter your full name: ")
# n = fullName.rfind(" ")
# print("Last name: ", fullName[n+1 : ])
# print("First name (s) :", fullName[ :n])

full_name = input("Enter your full name: ")
index_of_space = full_name.rfind(" ")
first_name = full_name[:index_of_space]
last_name = full_name[index_of_space+1:]
print('First_name', first_name)
print("Last_name", last_name)


# index_of_space would = what kind of data type? A: 
# .rfind(" ") = what place in order is the "space" A: 5 as it is the 5th caracher in
# requires a space in this code to allow it to break up the in, i.e., if someone put in 50cent, the result would be 50cent twice

# annual_income = eval(input("What's yo income homie?: "))  # can use eval or int, or float
# print("Homie's income is", annual_income)
# monthy_income = annual_income/12   
# print("Monthly income is", monthy_income)

# looks like a number but it is a string!!! you get error code  unsupported operand type(s) for /: 'str' and 'int' A: can use evale to fix problem

# how to convert numbers back into sting. use str function

# var1 = 1
# var2 = 2
# var3 = "3"
# var4 = "4"

# var5 = var1-var2 #3 Int
# var6 = var3+var4 # 34 # String
# when in ("")'s the into is put togeather where as the
# the \ can be used as a continuation of a line of code

# str1 = "Python"

# length = len(str1) #5 Int

# str2 = str1[:] #the begining to the end -1 A: Pytho String\ take away the -1 to keep "Python"
# print("str2", str2)
# str3 = str1[:10] # error of out of range
# print("str3", str3)
# str4 = str2[2:-1] #tho
# print("str4", str4) # A: "th" becaues it starts from the first index and goes to the last

# git add .\ git branch\ git status
# knowing what stages your branch is currently on
# when use git add. it will show red if anything in the code was changed
# when you use git dif it will show you what has changed
