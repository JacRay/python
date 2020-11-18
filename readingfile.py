employ = open("calculator.py","r") #read information inside file
#open("hey.py","w") #write in file
#open("calculator.py", "a") 3 append file

if employ.readable():
    print(employ.readline())
    print(employ.readlines()[2])
    print(employ.read())

employ.close()