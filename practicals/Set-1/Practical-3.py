import random
pass_length = int(input("Enter the specific length for the password: "))
pass_book = "1234567890qwertyuiopasdfghjklzxcvbnm;',./!@#$%^&*QWERTYUIOPASDFGHJKLZXCVBNM"
print("The generated  Password is: ",''.join(random.sample(pass_book,pass_length)))