str1="hello " # string declare using ""
str2='world' #string declare using ''

final=str1+str2  # combine the both string into one string

print(final) # print combined string
 
str3='hello , my name is "Jack" , i am 20 years old.' # print the "" into the output string
print(str3)

str4='''hello
how are you'''  # '''content''' or """content""" is used for the multiple line string

print(str4)


str5="Hello elon"  
print(str5[0])   # it will print the index possition 0 element of the string str5
print(str5[1])   # it will print the index possition 1 element of the string str5
print(str5[2])   # it will print the index possition 2 element of the string str5
print(str5[3])   # it will print the index possition 3 element of the string str5
print(str5[4])   # it will print the index possition 4 element of the string str5

print("\nprint the string using for loop\n")
str6="Happy birthday"

for character in str6 :  # this for loop will repeat until all the element of the string will printed one-by-one
    print(character)