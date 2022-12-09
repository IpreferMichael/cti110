#Recipt for food items
#CTI-110
#9/27/22
#Michael Wright

food1 = str(input("Enter food item name:\n"))
food1P = float(input("Enter item price:\n"))
food1Q = int(input("Enter item quantity:\n"))

#get total cost
totalCost1 = food1P * food1Q

#Print recipt
print("\n\nRECEIPT")
print(food1Q, food1, "@ " '$'+f'{food1P:.2f}', '=', '$'+f'{totalCost1:.2f}')
print("Total cost: " '$'+f'{totalCost1:.2f}')

#Get input for second food item
food2 = str(input("\n\nEnter second food item name:\n"))
food2P = float(input("Enter second item price:\n"))
food2Q = int(input("Enter item quantity:\n"))

#find total cost for second food item
totalCost2 = food2P * food2Q
#find total cost for both items
finalCost = totalCost1 + totalCost2
#print second recipt for items
print("\n\nRECEIPT")
print(food1Q, food1, "@ " '$'+f'{food1P:.2f}', '=', '$'+f'{totalCost1:.2f}')
print(food2Q, food2, "@ " '$'+f'{food2P:.2f}', '=', '$'+f'{totalCost2:.2f}')
print('Total cost:', '$'+f'{finalCost:.2f}\n')

#calculate gratiuity
gratuity = .15 * finalCost

#print out recipt with gratuity + final total
print('15% gratuity:', '$'+f'{gratuity:.2f}')
print('Total with tip:', '$'+f'{finalCost + gratuity:.2f}')
