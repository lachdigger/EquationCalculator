def equationCalculator(equation):
    left = ""
    right = ""
    symbol = ""
    for i in range(0, len(equation)):
        if equation[i] == "+" or equation[i] == "*" or equation[i] == "-" or equation[i] == "/" :
            symbol = equation[i]
        elif(symbol == ""):
            left += equation[i]
        else:
            right += equation[i]

    if symbol == "+":
        return float(right) + float(left)
    elif symbol == "-":
        return float(left) - float(right)
    elif symbol == "/":
        return float(left)/ float(right)
    elif symbol == "*":
        return float(left) * float(right)
    else:
        return 0



inputEquation = input("Please enter the equation you wish to calculate.")
print(equationCalculator(inputEquation))
