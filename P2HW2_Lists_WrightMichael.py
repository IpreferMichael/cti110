#Making a simple list
#CTI-110
#P2HW2-List
#Michael Wright
#9/26/22
#

#Ask user for values
module1 = float(input('Enter grade for Module 1:'))
module2 = float(input('Enter grade for Module 2:'))
module3 = float(input('Enter grade for Module 3:'))
module4 = float(input('Enter grade for Module 4:'))
module5 = float(input('Enter grade for Module 5:'))
module6 = float(input('Enter grade for Module 6:'))

#create list
moduleList = [module1, module2, module3, module4, module5, module6]

#Print output for module list
print('\n------------Results------------')
#Get minimum value
print('Lowest Grade:    ', min(moduleList))
#Get max value
print('Highest Grade:   ', max(moduleList))
#Get sum of all values
print('Sum of grades:   ', sum(moduleList))
#Get Average by dividing sum of all values by 6 and limit answer to decimal places
print('Average:         ', f'{sum(moduleList) / 6 :.2f}')
print('---------------------------------')
