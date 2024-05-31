user_string = str(input("Enter a string to chek if its palindrome: "))
print("It is palindrome" if user_string == user_string[::-1] else "The string is not palindrome")