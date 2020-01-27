import time 
"5 names 5 numbers"
def n_1():
    print ("This program was made by \nAaron vandenberg")
    print ("_____________________")
    time.sleep (2)
    total = 0
    allnums = []
    allname = []
    for i in range (1,6):
        name = input ("Please enter a name : ")
        number = int(input ("Please enter a number : "))
        allnums.append(number)
        allname.append(name)
        total = (total+(number))
    var_1 = allnums.index(max(allnums))
    average = total / len(allnums)
    print ("The maximum mark was", allname[var_1] , "with" , max(allnums))
    print ("The average of all the numbers is",average)
n_1()

