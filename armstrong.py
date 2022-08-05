#for a given input - Check a number is an armstrong or not
#armstrong number is sum of the power each digit to the number of digits is equal to original number
#For ex - if the number is 123 , we check 1*1*1 + 2*2*2 + 3*3*3 is same as 123. 
#36 is not equal to 123. 123 is not Armstrong
#407 is a good example - 4*4*4 + 0*0*0 + 7*7*7 = 64 + 0 + 343 = 407


myNum = int(input("Enter a 3 digit number : "))
if(myNum > 999):
  print("Please enter a 3 digit number only")
else:
  checkNum = myNum 
  # check the digits of the number
  lenNum = len(str(myNum)) #Since, we are entering 3 digit number, it is always 3
  sumNum = 0
  #Loop thru each digit
  while myNum != 0:
	  remainingNum = lenNum % 10
	  sumNum = sumNum+(remainingNum**lenNum)
	  myNum = myNum//10
  if checkNum == sumNum:
	  print("The given number is armstrong number")
  else:
	  print("The given number is not armstrong number")

