#Driving Costs Part 2
#9/27/2022
#CTI-110
#Michael Wright

#1. Ask for miles per gallon, cost per gallon
milesPerGallon = 20
costPerGallon = 3.159

#2. Caculate cost per mile
#galsPerMile = 1 / milesPerGallon
#costPerMile = costPerGallon

costPerMile = costPerGallon / milesPerGallon

#3Multiply by number of miles
print("Cost to drive:")
print("20 miles:", '$'+f'{costPerMile * 20:.2f}')
print("75 miles:", '$'+f'{costPerMile * 75:.2f}')
print("500 miles: ", '$'+f'{costPerMile * 500:.2f}')
