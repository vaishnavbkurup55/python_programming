c = int(input("How many elements: "))
list1 = []

for i in range(c):
    list1.append(int(input("Enter the element: ")))

list1 = [i for i in list1 if i % 2 != 0]

print("List after removing even numbers:", list1)
