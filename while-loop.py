#while-loop

i=0
print("The initial value of i is : " , i)

while(i<=30):
    i=int(input("Enter the number :"))
    print(i)
    
print("Done with loop.")

print("=========================")

j=0
while(j<20):
    print(j+1 , end=" ")   # with end=" " you can customize what appears at the end of each print output.
    j+=1

print("\n=========================")

j=20
while(j>0):
    print(j , end=" ")   # with end=" " you can customize what appears at the end of each print output.
    j-=1


# in python there will be no existance of the do-while loop , so if you want to run and that type of code which use the do-while loop , then you need to write the content you writeen in loop again befor the loop once