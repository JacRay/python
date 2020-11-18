try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10/number
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)