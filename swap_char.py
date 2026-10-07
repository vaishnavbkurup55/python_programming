string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

new_string1 = string2[0] + string1[1:]
new_string2 = string1[0] + string2[1:]

print(new_string1 + " " + new_string2)
