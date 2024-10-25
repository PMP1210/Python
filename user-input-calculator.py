print("========== CALCULATOR ===========")

num1=float(input("Enter the 1st number :"))
num2=float(input("Enter the 2nd number :"))

print("\n\n")
print("Press 1 for addition. \nPress 2 for the subtraction. \nPress 3 for the multiplication. \nPress 4 for the division.")

choice=int(input("\n\nEnter your choice :"))

if(choice==1):
    print("\nSumation of " , num1 , "and" , num2 , "is =" , num1+num2)
elif(choice==2):
    print("\nSubtraction of " , num1 , "and" , num2 , "is =" , num1-num2)
elif(choice==3):
    print("\nMultiplication of ", num1 , "and" , num2 , "is =" , num1*num2)
elif(choice==4):
    print("\nDivision of " , num1 , "and" , num2 , "is =" , num1/num2)
else :
    print("\nYou enterd the invalid choice.")