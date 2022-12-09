#Calculating travel expenses
#9/25/22
#CTI-110 P1HW2 - Travel Expense
#Michael Wright
#

#print function of program
print('this program calculates and displays travel expenses')
#declare variables and get user input

budget = int(input('\nEnter Budget: '))

destination = str(input('\nEnter your travel destination: '))

gasMoney = int(input('\nHow much do you think you will spend on gas?'))

hotel = int(input('\nApproximately, how much will you need for accomodation/hotel?'))

food = int(input('\nLast, how much do you need for food?'))
#calculate travel budget and any money remaining
(travelBudget) = gasMoney + hotel + food
(leftOverBal) = budget - travelBudget

#print header
print('\n------------Travel Expenses------------')
#print results
print('Location:', destination)
print('Initial Budget: ', f'{budget:.1f}')
print('\nFuel:', f'{gasMoney:.1f}')
print('Accomodation: ', f'{hotel:.1f}')
print('Food: ', f'{food:.1f}')

print('\nRemaining Balance: ', f'{leftOverBal:.1f}')
