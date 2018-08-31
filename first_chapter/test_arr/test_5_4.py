#!/usr/bin/env python3.6

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]

num_value = input("Enter number in lists: ")

indx = 9 - num_list[::-1].index(int(num_value))

#print("[" + ", ".join([str(val) for val in num_list]) + "]")

print("[" + ", ".join([str(val) for val in num_list]) + "]" + " - index({})".format(indx))

word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_value = input("Enter name language programming: ")

indx = 7 - word_list[::-1].index(num_value)

print("[" + ", ".join(word_list) + "] - index({})".format(indx))
