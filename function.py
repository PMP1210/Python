#funtion is a set of code that perform a specific task

# mean function

def calculateMean(x,y):    # "def" it's a keyword to define the function used in user-define functions
    mean=(x*y)/(x+y)
    return mean

def biggerSmaller(x,y):
    if (x > y):
        return x
    else:
        return y
    
def timepass(x,y):
    pass                    # "pass" keyword is use to tell the compiler that ust skip this portion and comtinue to the next line of code without retuning the error
print("======== Calculate the mean of two numbers ========\n")
num1=int(input("Enter the value 1 : "))       # convert the input into the integer using "int" keyword
num2=int(input("Enter the value 2 : "))       # convert the input into the integer using "int" keyword

print("\nThe mean of " , num1 , " and " , num2 , " is = " , calculateMean(num1,num2))
print("\nFrom " , num1 , " and " , num2 , " the greater value is = " , biggerSmaller(num1,num2))
