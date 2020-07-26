def sum_two_number(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


while True:
    print('1. Sum:  ')
    print('2. Subtraction: ')
    print('3. Division: ')
    print('4. Multiplication: ')
    print('5. Exit')

    try:
        item = int(input("Select a number between 1 and 5: "))
    except:
        print("Your entered item is wrong. Please Select a number between 1 and 5:")
        print('#' * 40)
        continue

    if item not in range(1, 6):
        print('Wrong Number. Please Select a number between 1 and 5:')
        print('#' * 40)
        continue

    if item != 5:
        number_left = int(input("please insert a number: "))
        number_right = int(input("please insert another number: "))

    if item == 1:
        print("RESULT: ", sum_two_number(number_left, number_right))
        print('*' * 40)
    elif item == 2:
        print("RESULT: ", subtraction(number_left, number_right))
        print('*' * 40)
    elif item == 3:
        print("RESULT: ", division(number_left, number_right))
        print('*' * 40)
    elif item == 4:
        print("RESULT: ", multiplication(number_left, number_right))
        print('*' * 40)
    else:
        break

