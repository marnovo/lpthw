# Learn Python the Hard Way
# https://learnpythonthehardway.org/python3/ex7.html

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

# Prints string
print("Mary had a little lamb.")
# Formats string, replacing the {} with another string, then prints it all
print("Its fleece was white as {}.".format('snow'))
# Prints string
print("And everywhere that Mary went.")
# Prints a string (".") a number o times (10)
print("." * 10)  # what'd that do?

# Sets strings to variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# Prints strings concatenates together with no spaces, besides when end is set
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# Prints strings concatenates together with no spaces, besides when end is set
print(end7 + end8 + end9 + end10 + end11 + end12)
