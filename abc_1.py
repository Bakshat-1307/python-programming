try:
    a=5
    b='hello'
    print(a/b)
except TypeError:
    print('Typerror occurred')

try:
    a=5
    b=0
    print (a/b)
except ZeroDivisionError:
        print ('Division by zero not allowed')

try:
    x="Akshat"
    print(y)
except NameError:
        print("Namerror y is not defined")






