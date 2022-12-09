# CTI 110
# P5Lab-Leap Year
# Michael Wright
# 11/10/22

def days_in_feb(year):
    isLeap = False
    # can we divide evenly by 4
    if year % 4 == 0:
        # it might be
        isLeap = True
        # if it's a century, must be divisible by $
        if year % 100 == 0:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
    if isLeap:
        daysInFeb = 29
    else:
        daysInFeb = 28
    print(year, "has", daysInFeb, "days in February.")


def main():
    year = int(input("Enter a year: "))
    days_in_feb(year)



# start program
main()
