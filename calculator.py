print("select one operation to perform :")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")

operation = input()

if operation == "1":
    num1=int(input("enter first number :"))
    num2=int(input("enter second number : "))
    print("sum of the two numbers is :"+str(int(num1)+int(num2)))
elif operation == "2":
    num1=int(input("enter first number :"))
    num2=int(input("enter second number : "))
    print("difference of the two numbers is :"+str(int(num1)-int(num2)))
elif operation == "3":
    num1=int(input("enter first number :"))
    num2=int(input("enter second number : "))
    print("Multiplication of the two numbers is :"+str(int(num1)*int(num2)))
elif operation == "4":
    num1=int(input("enter first number :"))
    num2=int(input("enter second number : "))
    print("division of the two numbers is :"+str(int(num1)/int(num2)))
else :
    print("invalid entry")

    