#Unit Test 2 - Write Program to do addition and Subtraction
# of two numbers using functions

def addNum(x,y):
  return x+y

def subNum(x,y):
  return x-y

firstNum = int(input("Enter first Number : "))
secondNum = int(input("Enter Second Number : "))

print('adding the numbers : ', addNum(firstNum, secondNum))
print('subtracting the numbers : ', subNum(firstNum, secondNum))
