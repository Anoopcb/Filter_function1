## Filter function

number = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]

def is_even(a):

    return a%2==0

number1 = list(filter(is_even, number))
print(number1)

number2= list(filter(lambda a:a%2==0, number))
for num in number2:
    print(num)
print(number2)
umber2= list(filter(lambda a:a%2==0, number))
for num in number2:
    print(num)