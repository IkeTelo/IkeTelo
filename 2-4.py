# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2+ num3
# print("Sum is {0:n}" .format(sum_of_all_numbers))

# list_of_numbers = [1, 10, 1000]

# print(list_of_numbers)
# list_of_numbers.clear()
# print(list_of_numbers) # []

# # what is a list? -lame mans terms aka an Aray = a container that holds stuff; i.e., ints, var, charachters, strings, other list.
# #  each item in list is an item, fitst in item is 0 last item in list is -1

# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# print(list_of_numbers)

# list_of_numbers2 = [3, 100, 5] # when you see "[]" it is an empty list

# list_of_number3 = list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers)
# adding/connecting arrays using +
# l1 = [1, 32, 4]
# l2 = [100, 200, 300]
# l3 = l1 + l2
# print(l3)
# # removing items from list using del
# # del team(-1) is referring to removing the last item in array
# team = ("Seahawks", 2014, "CenturyLink Field")
# nums = [5, 10, 5, 5]
# words = ["spam", "ni"]
# del team[-1]
# words = ("Spam", "Wink", "HI")
# words.insert(1, "Hello")
# print("Words ====>", words)
# # calculate average of grades
# grades = [] #creating the variable grades and assign it the empty list.
# num = float(input("Enter the first grade: "))
# grades.append(num)
# num = float(input("Enter the second grade: "))
# grades.append(num)
# num = float(input("Enter the third grade: "))
# grades.append(num)
# num = float(input("Enter the fourth grade: "))
# grades.append(num)
# # average = sum(grades) / len(grades)
# # print("Average Grade: {0: .2f}" .format(average))
# grades.append(num)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# average = sum(grades) / len(grades)
# print("Average Grade: (0: .2f)" .format(average))
# grades.append(1)
# grades.append(2)
# grades.append(4)
# grades.append(9)
# print("grades", grades)
# length = len(grades)
# print("length", length)
# print("sliced", grades[0:2])
# list1 = ["a, b, c, d, e, f"]
# list1[2:len(list1)]

# Splits and join methos
# print("a,b,c" .split(','))
# print("a**b**c" .split('**'))
# print("a/nb/nc" .split())
# print("a b c" .split())
# str1 = "a, b, c"
# parts = "a, b, c,".split(",")

# print("parts ", parts)

# lines = ["To", "Be", "Or", "Not", "To", "Be"]

# print("lines before joint ", lines)

# joined = "-".join(lines)

# print("joined ", joined)

# open up the Data.txt filw in read mode
# infile = open("Data.txt", "r")

# print("infile", infile)
# names = []
# for line in infile:
#     # print("line: ", line)
#     # print("line after swapping the right side: ", line.rstrip())
#     names.append(line.rstrip())

# print("names: ", names)
# # close the Data.txt file to preserve memory

# names_using_comprehension = [line.rstrip() for line in infile]

# print("names_using_comprehension: ", names_using_comprehension)

# infile = open("Grades.txt", "r")
# for lines in infile:
#     print("line: ", lines.rstrip())

# infile.close()

# infile = open("Grades.txt", "r")
# list_of_numbers = [eval(line) for line in infile]
# infile.close()

#  to create a tuple use ()'s insead of [] tuple is inmutable(not modifiable)

# list_of_names = ("Lucus", "Isaac", ["A", (1, 2, 3), "C"])

# print("list_of_names", list_of_names[2][1](-1))

# L = [5, 6]
# n = 2
# s = "Python"
# t = ('a', 'b', 'c')
# L.append(7)
# n += 1
# s = s.upper()
# t = t[1:]

list1 = ("A", "B", "C")

list2 = list(list1)

list2.append("D")

print("List1", list1)
print("List2", list2)
