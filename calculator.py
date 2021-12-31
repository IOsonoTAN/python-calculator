inputNumber1 = input('Enter number 1\n')
inputCondition = raw_input('Enter condition\n')
inputNumber2 = input('Enter number 2\n')

number1 = int(inputNumber1)
number2 = int(inputNumber2)

sumNumbers = 0
if (inputCondition == '+'):
  sumNumbers = number1 + number2
elif (inputCondition == '-'):
  sumNumbers = number1 - number2
elif (inputCondition == '*'):
  sumNumbers = number1 * number2
elif (inputCondition == '/'):
  sumNumbers = number1 / number2

result = (number1, inputCondition, number2, sumNumbers)

print("Result of %i %s %i = %i" % result)
