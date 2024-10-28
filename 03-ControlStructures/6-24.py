###
# Write a program that creates the following pattern
#
pattern = ("*")
while len(pattern) <= 5:
    print(pattern)
    pattern += "*"
while len(pattern) > 1:
    pattern = pattern [:-1]
    print(pattern)