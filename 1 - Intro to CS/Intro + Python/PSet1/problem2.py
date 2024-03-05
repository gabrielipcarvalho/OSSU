# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2
s = ""
bob = 0
for i, ch in enumerate(s):
    if i == len(s) - 2:
        break
    if ch == "b" and s[i + 1] == "o" and s[i + 2] == "b":
        bob += 1
    counter += 1
print(bob)