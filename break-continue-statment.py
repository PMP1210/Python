# break

for i in range(1,13):
    if(i==11):
        break        # in loop it will rum 12 times but when it will run 11th time with i=11 then it will go inside the if condition and break the loop and comes out of it
    print("3" , "*" , i , "=" , 3*i)

print("I came out of the loop when i touch the value of i=11  !!!!!!")


# continue

colours=["red" , "green" , "blue" , "yellow"]
for color in colours:
    if(color=="green"):
        continue     # when "color" match with the green then it will don't print the color and continiue with the next increment but don't break the loop
    print(color , end=" ")
    