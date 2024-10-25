#there are two types of type-casting
#1. explicit (user need to change type manually) , 2. implicit (pythom change the type on itself)

#1.explicit

a="10" #string
b="20" #string

print("Type of a =",type(a))
print("Type of b =",type(b))

print("Sum of" , a , "&" , b , "=" , int(a) + int(b) ) #convert botth string in iint and aa the number

#2.implecit

c=9.5  #float
d=10 #int

print(type(c))
print(type(d))

print(c+d) #sum the both number and give float number in output
print("Total's type :" , type(c+d))