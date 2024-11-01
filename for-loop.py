# for-loop for striing

str="Ashish"

for i in str :  # it will rpint the all the character of the str string one by one
    print(i)

print("==================")

for i in str :
    print(i , end=" ")  # it will print all the characters of the string one by one in one line but give some space beetween  each charachter


print("\n==================")
# for-loop for list

colours = ["Red" , "Green" , "Blue" , "Yellow"] # list of the different colours

for color in colours :
    print(color)   # it will print each color name one by one and give a new line between each color name

print("\n==================")

for color in colours :
    print(color) 
    for i in color :
        print(i)  # it will print the each character of the captured string ferom the list one by one


# range function in for-loop
# the for loop's range function contains three elements : "start" , "stop" , "step".
# syntex :- for variable in range (start,stop,step):


for i in range(10): # it will run 10 times 
    print(i)     # it will print the i value from 0 to 9

print("\n==================")

for i in range(1 , 11) :     # it will run 10 times 
    print(i)    # ti will replace the by default i value 0 with 1 and print till it will reach the value of 11

print("\n==================")

for i in range (1 , 11 , 3):  # it will run 10 times
    print(i)    # it will print from 1 to 10 values with the skip of 2 values and then print the 3rd value in loop till end

print("\n==================")
# table using for-loop

value=int(input("Enter the number which you want to generate the table :"))  # take input for the tbale number

for i in range(1,11):
    print(value , "*" , i , "=" , i*value)    # simple output design with the output value