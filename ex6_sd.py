# Learn Python the Hard Way
# https://learnpythonthehardway.org/python3/ex6.html

# Sets variable value to 10
types_of_people = 10
# Sets x variable value to (formatted) string w/ variable value inside
x = f"There are {types_of_people} types of people."  # str in str

# Sets variable to string
binary = "binary"
# Sets variable to string
do_not = "don't"
# Sets y variable value to (formatted) strings w/ variable values inside
y = f"Those who know {binary} and those who {do_not}."  # str in str

# Print string x
print(x)
# Print string y
print(y)
# Print (formatted) string w/ x variable value inside
print(f"I said: {x}")  # str in str
# Print (formatted) string w/ y variable value inside
print(f"I also said: '{y}'")  # str in str

# Sets variable to boolean False
hilarious = False
# Sets variable to a not formatted string, thus {} is not evaluated here
joke_evaluation = "Isn't that joke so funny?! {}"  # str in str?
# Prints evaluated string with 'hilarious' variable content evaluated in {}s
print(joke_evaluation.format(hilarious))

# Sets variable w to string
w = "This is the left side of..."
# Sets variable e to string
e = "a string with a right side."

# Prints both variables concatenated (notice no space is added like w/ commas)
print(w + e)

# Study Drills

# 1. Go through this program and write a comment above each line explaining it.
# 2. Find all the places where a string is put inside a string. There are four places.
# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# 4. Explain why adding the two strings w and e with + makes a longer string.
# A: Adding strings concatenates them w/o spaces in between
