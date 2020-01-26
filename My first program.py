import time
print ("Hello welcome to Aaron's Price Check")
inputs1 = input("We will need some inputs from you is that fine : ")
 
if (inputs1 == "yes" or "y" or "sure"):
    print ("Thank , you let's continue")   
else :
       print ("error 5904234324234252409847908437947493733947549273549273590243790143279014732154279417542904153790153794013579513724913572490153247153427813597428780135974088154270818305-40925189077777777777777777777777777777777711111111111111111111111111111111111111111111111111111111111111111111111111111111111113029572035")
time.sleep (3)
 
product1 = input ("Please enter the name of your first product : ")
product2 = input ("Please enter the name of your second product : ")
product3 = input ("Please enter the name of your third product : ")
print ("processing the information thank you ... ")
time.sleep (5)
 
print ("please give us the following information : ")
price1 = int(input( "What is the price of " + product1 + "? : " ))
time.sleep (2)
price2= int(input( "What is the price of " + product2 + "? : " ))
time.sleep (2)
price3 = int(input( "What is the price of " + product3 + "? : " ))
 
wants_total = input ("Want us to add the prices together and give the average \ncost price of the items : ")
total = (price1 + price2 + price3)
average = (total // 3)
if (wants_total =="yes"):
    time.sleep (5)
    total == (price1 , price2 ,price3)
    average = total /3
 
print ( "the total of " + product1  + " and " + product2  + " with " + product3  + " is " + "zar " + str(total)  + " and the average is " + "zar" + str(average))