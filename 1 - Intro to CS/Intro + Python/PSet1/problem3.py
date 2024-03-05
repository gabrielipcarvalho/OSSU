# Problem 3
# 1 point possible (ungraded)
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

#### OLD VERSION:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# string = ""
# final_string = ""
# index = -1
# for c in s:
#     for j, ch in enumerate(alphabet):
#         if c == ch:
#             if j >= index:
#                 index = j
#                 string += ch
#                 if len(string) > len(final_string):
#                     final_string = string
#             else:    
#                 index = j
#                 string = ch
# print("Longest substring in alphabetical order is:", final_string)

#### UPDATED VERSION:
string = ""
final_string = ""
for i, c in enumerate(s):
    if string == "" or c >= s[i-1]:
        string += c
        if len(string) > len(final_string):
            final_string = string
    else:
        string = c
print("Longest substring in alphabetical order is:", final_string)