print("This program calculates the tip and tell how much each person has to pay")
#Greeting
print("Welcome to the tip calculator!")
#Asking for total bill
totalBill= float(input("What was the total bill? "))
#Asking for percentage of tip
tipPercentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Asking for total bill payers
billPayers = int(input("How many people to split the bill? "))
#Calculating the tip
tipAmount = totalBill*tipPercentage/100
#Calculating total bill including tip
finalBill = totalBill + tipAmount
#Splitting the bill between people
billSharedAmount =  round(finalBill/billPayers, 2)
#Outputting the result
print(f"Each person should pay: ${billSharedAmount}")