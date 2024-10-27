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