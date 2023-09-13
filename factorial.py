# code for computing factorial

number = 5
result = 1
if number < 0:
    print('Error!')
elif number == 0:
    print('Factorial of 0 is 1')
else:
    for i in range(1, number+1):
        result = result * i
    print('Factorial of', number , "is", result)

