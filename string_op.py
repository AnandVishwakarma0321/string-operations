# Use quotation marks for defining string

"Michael Jackson"

# Use single quotation marks for defining string

'Michael Jackson'

# Digitals and spaces in string

'1 2 3 4 5 6 '

# Digitals and spaces in string

'1 2 3 4 5 6 '

# Print the string

print("hello!")

# Assign string to variable

Name = "Michael Jackson"
Name

# Print the first element in the string

print(Name[0])

# Print the element on index 6 in the string

print(Name[6])

# Print the element on the 13th index in the string

print(Name[13])

# Print the last element in the string

print(Name[-1])

# Print the first element in the string

print(Name[-15])

# Find the length of string

len("Michael Jackson")

# Take the slice on variable Name with only index 0 to index 3

Name[0:4]

# Take the slice on variable Name with only index 8 to index 11

Name[8:12]

# Take the slice on variable Name with only index 8 to index 11

Name[8:12]

# Get every second element. The elments on index 1, 3, 5 ...

Name[::2]

# Get every second element in the range from index 0 to index 4

Name[0:5:2]

# Concatenate two strings

Statement = Name + "is the best"
Statement


# Print the string for 3 times

3 * "Michael Jackson"

# Concatenate strings

Name = "Michael Jackson"
Name = Name + " is the best"
Name

# New line escape sequence

print(" Michael Jackson \n is the best" )

# Tab escape sequence

print(" Michael Jackson \t is the best" )

# Include back slash in string

print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )

# Convert all the characters in string to upper case

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Convert all the characters in string to upper case

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output

Name = "Michael Jackson"
Name.find('el')

# Find the substring in the string.

Name.find('Jack')

# If cannot find the substring in the string

Name.find('Jasdfasdasdf')

#Consider the variable D use slicing to print out the first three elements:

D = "ABCDEFG"
print(D[0:3])

#Use a stride value of 2 to print out every second character of the string E:

E = 'clocrkr1e1c1t'
print(E[::2])

#Print out a backslash:
print("\\")

#Convert the variable F to uppercase:

F = "You are wrong"
print(F.upper())

#Consider the variable G, and find the first index of the sub-string snow:
G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(G.find("snow"))

#In the variable G, replace the sub-string Mary with Bob:
G.replace('Mary','Bob')