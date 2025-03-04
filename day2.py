# 1. Reverse a String
print(input("Enter a string: ")[::-1])

# 2. Check if a String is a Palindrome
string = input("Enter a string: ")
print(string == string[::-1])

# 3.Remove Duplicates from a String
print(''.join(set(input("Enter a string: "))))
 
# 4.Find the Longest Word in a String
print(max(input("Enter a string: ").split(), key=len))

# 5.Find Common Elements Between Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)
print(set(tuple1) & set(tuple2))


# 6.Find the Maximum and Minimum Value in a Dictionary
my_dict = {"a": 10, "b": 20, "c": 5} 
print(max(my_dict.values()), min(my_dict.values()))

# 7- Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)


# 8- Find Common Keys in Two Dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
print(set(dict1) & set(dict2))

# 9- takes a string and prints the longest
s = input("Enter a string: ")
print(max([s[:i+1] for i in range(len(s)) if s[:i+1] == ''.join(sorted(s[:i+1]))], key=len))
