#CTI 110
#11/1/22
#P4HW1-Grades
#Michael Wright

#Ask the user for 6 grades for the 6 modules
#Add them to a list.

grades = []

#grade1 = int(input("Enter grade for Module1:"))
#grades[0] = grade1

for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("The grades you entered are: \n", grades)
print("\n")
#Max and Min grades in list

print("The highest grade is:", max(grades))
print("The lowest grade is: ", min(grades))

#Now the average - divide the sum by the length(count)
total = sum(grades)
count = len(grades)
average = total / count
print("Sum of Grades:       ", total)
print("Average:             ", f'{average:.2f}')
