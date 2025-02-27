# Question 4
#27-02-2025
a =float(input("Enter First Number:"))
b =float(input("Enter Second Number:"))
operator=input("What you want to perform: { + , - , * , / , % }") #python takes input as string by default

if operator == "+" :
    print(f"{a} {operator} {b} =",a+b )
elif  operator == "-" :
    print(f"{a} {operator} {b} =",a-b )
elif operator == "*" :
    print(f"{a} {operator} {b} =",a*b )
elif operator == "/" :
    
    if b!=0:
        print(f"{a} {operator} {b} =",a/b )
    else:
        print("Error! Division by zero. ")
elif operator == "%":
    print(f"{a} {operator} {b} =",a%b )

else:
    print("Invaild Operator")
