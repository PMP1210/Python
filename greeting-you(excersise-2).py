import time # import the time librery

name=str(input("Enter yoyr name : ")) # tkae a name as an input as a string
timecurrent=time.strftime('%H:%M:%S') # generate current time using locaL COMPUTER
print("Current time is : " , timecurrent) # print the current time which generated

if (timecurrent >= '06 : 00 : 00' and timecurrent <= '12 : 00 : 00'):
    print("Good morning " + name)
elif (timecurrent >= '12 : 00 : 01' and timecurrent <= '16 : 00 : 00'):
    print("Good afternoon " + name)
elif (timecurrent >= '16 : 00 : 01' and timecurrent <= '20 : 00 : 00'):
    print("Good evening " + name)
else :
    print("Good night " + name)