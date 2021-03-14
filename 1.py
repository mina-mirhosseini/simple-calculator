import math
print("enternumber1")
number1 = float(input())
print("enter operator")
operator = input()
if(operator == 'sin' or operator == 'cos' or operator == 'tan' or operator == 'cot'):
    number1 = math.radians(number1)
elif(operator != 'log' and operator != 'sqrt'):
    print("enter number2")
    number2 = float(input())

if (operator == "sin"): 
    result = math.sin(number1)
elif (operator == "cos"):
    result = math.cos(number1)
elif (operator == "tan"):
    result = math.tan(number1)
elif (operator == "cot"):
    result = 1/math.tan(number1)
elif (operator == "log"):
    result = math.log(number1)
elif (operator == "sqrt"):
    result = math.sqrt(number1)
elif (operator=="+"):
    result=number1+number2
elif (operator=="-"):
    result=number1 - number2
elif(operator=="*"):
    result=number1*number2
elif(operator=="/"):
    if (number2==0) :
        result="error"
    else :
        result=number1/number2
elif(operator=="^"):
    result=number1**number2
else:
    result = "invalid operator"


print(result)
print("test git")

