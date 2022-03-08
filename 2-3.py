# print("chapter 2-3")
# # print("Hello", "World", sep="**")
# print("one", "two", "three", sep=", ")

# print("Hello", end=" ") #the end=" " allows the two separate print commands to go togeather
# print("World")
# # \t induces a horizontal tab
# # \n induces a newline operation

print("a\tb\tc")
print("a\tb\tc" .expandtabs (5))
print("Nudge, \tnudge, \nwink, \twink, " .expandtabs (11))

print("Hello World") #"Hello World" to get the ""s to pop up with hello world, you can use ' ex. print('"Hello World"') or \ ex. print("\"Hello World\"")
print("\"Hello Wolrd!\"")
print("\\Hello World!\\") #this will disply the backslashes on the terminal

# justifing output in a field

print("0123456789012345678901234567")
print("Rank".1just(5), "Player" .1just(20), "HR" .rjust(3), sep="")
print('1'.center(5))

# String Variables- string value, fist time assigned, print statement w/out ""'s
# Indices and Slices- Position or index of charachert in string, i.e., spam & eggs