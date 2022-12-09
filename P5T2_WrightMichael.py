# CTI 110
# P5T2 - Basketball Offense
# Michael Wright
# 11/10/22

# Very simple basketball simulator

import random

def offense():
    """
    offense() - simulates one play in basketball
    arguments: none
    returns: none
    """
    print("You're on offense.")
    print("Type pass or shoot.")
    command = input("> ")
    print("You chose", command)
    if command == "shoot":
        #can score or miss
        #score -> other team takes possesion
        #miss -> random chance who gets it
        print("He shoots...")
        # 50/50 chance
        roll = random.randint(1, 100)
        print("rolled", roll)
        if roll >= 50:
            print("...and it's good! 2 points!")
            # hand over posession
            return
        else:
            print("...it's no good!")
            return
    if command == "pass":
        #either success, or turnover
        print("Ball passed...")
        # keep going
        offense()

def main():
    print("Now simulating one play.")
    offense()





# start program
main()
