#Simple Calculator Program
def calc():
    try:
        x=float(input("Enter a number to be operated with:"))
        op=input("Enter an operator(+,-,*,/):")
        y=int(input("Enter another number to be operated with: \n"))
        
        if op=="+":
            print(x+y)
        elif op=="-":
            print(x-y)
        elif op=="*":
            print(x*y)
        elif op=="/":
            print(x/y)
    except ZeroDivisionError:
        print("Oops, you maybe trying to divide the number by zero")
    else:
        print("oops, invalid operator")
        
calc()
