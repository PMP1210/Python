# strings are immutable

str1="Hello !!!!"

print(str1.upper()) # it will print all the charactrers of the string in upper case
print(str1.lower()) # it will print all the characters of the string in lower case

print(str1.rstrip("!")) # it will remove all the "!" from the string until it's after the content(Hello)

print(str1.replace("Hello" , "How")) # it will replace the content

print(str1.split(" ")) # it will make a saperate list of the string after each space

str2="introduction to the python programmin."
print("This is without capitalization :" , str2)
print("This is with capitalization :" , str2.capitalize()) # it will capitalize the first character of the string