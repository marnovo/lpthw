# Learn Python the Hard Way
# https://learnpythonthehardway.org/python3/ex8.html

# Study Drills

# 1. Go back through and write a comment on what each line does.
# 2. Read each one backward or out loud to find your errors.
# 3. From now on, when you make mistakes, write down on a piece of paper what
#    kind of mistake you made.
# 4. When you go to the next exercise, look at the mistakes you have made and
#    try not to make them in this new one.
# 5. Remember that everyone makes mistakes. Programmers are like magicians who
#    fool everyone into thinking they are perfect and never wrong, but it's all 
#   an act. They make mistakes all the time.

# Sets variable formatter to string with 4 {}s
formatter = "{} {} {} {}"

# Formats string formatter passing each number integer to a {} and prints them
print(formatter.format(1, 2, 3, 4))
# Formats string formatter passing each number string to a {} and prints them
print(formatter.format("one", "two", "three", "four"))
# Formats string formatter passing each Boolean to a {} and prints them
print(formatter.format(True, False, False, True))
# Formats string formatter passing each formatter string to a {} and prints them
print(formatter.format(formatter, formatter, formatter, formatter))
# Formats string formatter passing each string to a {} and prints them
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
