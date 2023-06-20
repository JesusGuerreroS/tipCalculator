########################################################################################
#this script allows calculates splitting the bill between people and with a chosen tip##
########################################################################################


print("Welcome to the tip calculator!")

#receiving the corresponding values
bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: "))
quantity = int(input("How many people to split the bill?: "))

#doing the calculation
calculation = round((bill / quantity) * (1 + (tip / 100) ), 2) 

#printing the calculation
print(f"Each person should pay: ${calculation}")
