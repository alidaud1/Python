#Basic Arithmetic Operations

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation to be performed: (+ , - , * , /)")
if (operation=='+'):
  print("Addition is: ",num1+num2)
if(operation=='-'):
  print("Subtraction is: ",num1-num2)
if(operation=='*'):
  print("Multiplication is: ",num1*num2)
if(operation=='/'):
  print("Division is: ",num1/num2)