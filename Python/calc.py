print ("Hello World!")

def sum(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

def mult(op1, op2):
    return op1 * op2

def divide(op1, op2):
    return op1 / op2

def menu():
    print(" Menu")
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print("[x] - Exit")

print("-" * 30)
print(' Welcome to PyCalc')
print("-" * 30)

opc = ""
while(opc != "x"):
    menu()
    opc = input("Select an option: ")
    if(opc == "x"):
        break #break the loop
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if(opc == '1'):
        sum_res = sum(num1, num2)
        print("sum = " + str(sum_res))
    
    if(opc == '2'):
        minus_res = minus(num1, num2)
        print("sum = " + str(minus_res))

    if(opc == '3'):
        mult_res = mult(num1, num2)
        print("sum = " + str(mult_res))

    if(opc == '4'):
        divide_res = divide(num1, num2)
        print("sum = " + str(divide_res))

print("Thank you for using PyCalc")