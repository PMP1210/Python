a=20
b=10
print("a : " , a)
print("b : " , b)

print("\nPress '+' for addition. \nPress '-' for the subtraction. \nPress '*' for multiplication. \nPress '/' for the division. \nPress '%' for the modulus. \nPress '^' for the square.")
operator=(input("\nEnter the operation you want to perform :"))

match operator:                          # switch case in python , and remember that it's not madnetory in match-case in python to use the break statment like a C,C++
    case '+': 
        print("A + B = ", a+b)
    case '-':
        print("A - B = ", a-b)
    case '*':
        print("A * B = ", a*b)
    case '/':
        print("A / B = ", a/b)
    case '%':
        print("A % B = " , a%b)
    case _ if operator == '^':                      # you can also use the if condition with default case
        print("A ^ B =" , a**b )
    case _:                                             # '_' is used for the default choice
        print("You entered invalid operator.")