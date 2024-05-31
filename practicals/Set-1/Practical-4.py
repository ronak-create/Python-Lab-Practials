list_len = int(input("Enter the length of the element list: "))
marks_list = [int(input("Enter value: ")) for i in range(list_len)]
avg = sum(marks_list)/list_len
print("There for the Average of the list of elements is: ",avg)
