#if-else

print("========== VOTING ===========")
age=int(input("Enter your age :")) # tkae age as an input in integer

if (age >= 18):
    print("You are aligible for the voting.")
else :
    print("You are not aligible for the voting.")


# if-else ladder

print("========== CALCULATOR ===========")

num1=float(input("Enter the 1st number :")) #take input in float
num2=float(input("Enter the 2nd number :")) #take input in float

print("\n\n")
print("Press 1 for addition. \nPress 2 for the subtraction. \nPress 3 for the multiplication. \nPress 4 for the division.") # give choice to user to which operation they wants to perform in both input numbers

choice=int(input("\n\nEnter your choice :")) # take choice input from user in integer

if(choice==1):
    print("\nSumation of " , num1 , "and" , num2 , "is =" , num1+num2) # if choice is 1 then perform '+'
elif(choice==2):
    print("\nSubtraction of " , num1 , "and" , num2 , "is =" , num1-num2) # if choice is 2 then perform '-'
elif(choice==3):
    print("\nMultiplication of ", num1 , "and" , num2 , "is =" , num1*num2) # if choice is 3 then perform '*'
elif(choice==4):
    print("\nDivision of " , num1 , "and" , num2 , "is =" , num1/num2) # if choice is 4 then perform '/'
else :
    print("\nYou enterd the invalid choice.")  # if user enter the choice out of 1,2,3,4 then it will show this error message.


# nested if-else

print("========== PESONALITY ===========")

num=int(input("Enter your age :"))  # take age in integer
gender=str(input("Enter yout gender :")) # take gender in string

if (num >= 18):
    if gender in ["male" , "Male" , "m" , "M"]: 
        print("You are a men.")
    elif gender in ["Female" , "female" , "f" , "F"]:
        print("You are female.")
    else :
        print("You are other.")
else :
    print ("You are a child.")