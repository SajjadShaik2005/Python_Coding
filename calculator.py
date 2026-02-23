operator=input("Enter an operator (+ - * /): ")
input1=float(input("Enter first number: "))
input2=float(input("Enter second number: "))

if operator=='+':
    print(input1+input2)
elif operator=='-':
    print(input1-input2)
elif operator=='*':
    print(input1*input2)
elif operator=='/':
    print(input1/input2)
else:
    print(f"Invalid operator {operator}")
