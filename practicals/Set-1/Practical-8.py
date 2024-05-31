list_len = int(input("Enter the length of the list: "))
list1eles = [int(input("Enter a value: ")) for i in range(list_len)]
print(list1eles)
operation = int(input("Enter the operation you wan't to perform on this list:\n1. Arrange in ascending order.\n2. Arrange in descending order.\n"))
if operation == 1:
    print(sorted(list1eles))
else:
    print(sorted(list1eles,reverse=True))