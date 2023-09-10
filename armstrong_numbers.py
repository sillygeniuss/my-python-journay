def is_armstrong_number(number):
    count = 0
    length = str(number).__len__()
    for i in range(0, length):
        digit = int(str(number)[i])
        count += int(digit) ** length
    if count == number:
        return True
    else:
        return False
