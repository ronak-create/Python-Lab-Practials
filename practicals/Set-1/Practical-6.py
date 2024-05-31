fact_of = int(input("Enter a number to calculate factorial: "))
fact = 1
for i in range(1,fact_of+1):
    fact*=i
print(f'The factorial of {fact_of} is: {fact}.')