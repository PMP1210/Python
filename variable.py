a=10  #declare the integer value to the variable name "a" and "b"
b=30.20
d="work"

print("Sum of" , a , "&" , b , "is" , a+b)

print("Multioplication of " , a , "&" , b , "is" , a*b)

# if - else statement

c=10

if (c > 0) :
    print(c , "is possitive number.")
elif (c < 0):
    print(c , "is negative number.")
else :
    print(c , "is zero")

print(d)
print(type(a) , type(b) , type(d))

list1=[1,2.3,"vivek",[4,5]]  #list which strore the multiple types of data even store a list in itself , and list can be modifyed after the declaration during the execution so it is muttable
print(list1)

tuple1=(1,2.3,"vivek",('parrot','peacoke')) #tuple which also strore the multiple types od data even tuple itself , and tuple can't be modify after the declaration during the execution so it si immutable
print(tuple1)

dis={"name":"rocky" , "age":"19" , "std" : "12"} #dictionary will be unoredered collection of data which containing keyvalues pair
print(dis) 

