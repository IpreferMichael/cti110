# CTI 110
#P2LAB3 - Food Receipt
#Michael Wright
#9/29/22


#Declare Variables
foodName = str(input('Enter food item name:\n'))
foodPrice = float(input('Enter item price:\n'))
foodQuantity = int(input('Enter item quantity\n'))
#calulate total cost for price * quantity
totalCost = foodPrice * foodQuantity

#Print recipt for customer
print('\n\nRECEIPT')
print(foodQuantity , foodName, '@', '$'+f'{foodPrice:.2f}', '=', '$'+f'{totalCost:.2f}')
print('Total Cost: ', '$'+f'{totalCost:.2f}')