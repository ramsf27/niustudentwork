#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

tryAgain = "Yes"

while tryAgain =="Yes":
    
# get input from the user
    milesDriven = float(input("Enter miles driven:       "))
    gallonsUsed = float(input("Enter gallons of gas used:  "))
    CostPerGallon = float(input("Enter cost per gallon:  "))

    if milesDriven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallonsUsed <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif CostPerGallon <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((milesDriven / gallonsUsed), 2)
        ttlGasCost = round(gallonsUsed * CostPerGallon, 1)
        costPerMile = round(ttlGasCost / milesDriven, 1)
        print()
        print("Miles Per Gallon:     ", mpg)
        print("Total Gas Cost:      ", ttlGasCost)
        print("Cost Per Mile:        ", costPerMile)
        print()
        print()

    tryAgain = input("Would you like to try again?(Yes)?")
    print()
print("Bye")



