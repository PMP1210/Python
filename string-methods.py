# strings are immutable

str1="Hello !!!!"

print(str1.upper()) # it will print all the charactrers of the string in upper case
print(str1.lower()) # it will print all the characters of the string in lower case

print(str1.rstrip("!")) # it will remove all the "!" from the string until it's after the content(Hello)

print(str1.replace("Hello" , "How")) # it will replace the content

print(str1.split(" ")) # it will make a saperate list of the string after each space

str2="introduction to the python pRogrammin."
print("This is without capitalization :" , str2)
print("This is with capitalization :" , str2.capitalize()) # it will capitalize the first character of the string and make all the other character in

str3="welcome"
print("Without center keyword :" , str3)
print("the length of welcome is :" , len(str3)) # print the length of str3
print("With center keyword :" , str3.center(50)) # it will add the 43 space befor the string start and make the length of the string total 50
print("The lenght of welcome with centrer keywork :" , len(str3.center(50))) 
print("string with design center keyword :" , str3.center(50 , ".")) # it will add the "." befor & after the string with total length of 50

str4="Apple"
print(str4)
print("The count of \"p\" in the string is :" , str4.count("p")) # it will display how much time the "p" will be reapeted in string

str5="mango is my favourite fruit"
print("The 'mango' is end with '.' is :" , str5.endswith(".")) # if string will end with "." then it will return true otherwise it will return false
print("The string 'o is my' is end with 'my' is :" , str5.endswith("my" , 4 , 11)) # if 'o is my' is end with 'my'  then it will return true otherwise it will return false
print("The 'my' is at the index of  :" , str5.find("first")) # it will find the 'my' in the str5 string and return it's index possition
index=[i for i , char in enumerate(str5) if char == "a"] # it will make a list in which the 'enumerate' will create the goup of the char & it's index , and by check the char it will store the matched char index in list , and strore it in index as a list
print("In str5 the 'a' is at this index :" , index) # it will print the list of multiple index
print("This string is alphanumeric :" , str5.isalnum()) # it will check the A-Z , a-z , 0-9 in string is available then true otherwise any special character and space then false
print("This string is alpha :" ,str5.isalpha()) # it will check the A-Z & a-z only not special character, space and numbers

str6="world  world\n"
print("This string is lower :" , str6.islower()) # it will check string is totally in lower case or not
print("This string is printable :" , str6.isprintable()) # it will check all the characters are able to print or not
print("This string contains space :" , str6.isspace()) # it will check the space is availabe or not in string

str7="Organization Program studio"
print("This string is tittle :" , str7.istitle()) # it will check the all the words's first character is capital then return true
print("Convert into tittle :" , str7.title()) # convert all the word's first character into uppercase
print("This string is upper case :" , str7.isupper()) # it will check the all charaters are capital
print("Strat with :" , str7.startswith("Organization")) # check the starting of the string

str8="Wello"
print("Without replace :", str8)
print("Replaced string :" , str8.replace("Wello", "Hello")) # replace the content with new one provided
print("Swaped :" , str8.swapcase()) # it will convert the smaller into capital & capital into smallerW 