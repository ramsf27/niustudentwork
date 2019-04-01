#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
milesDriven = float(input("Enter miles driven:\t\t"))
gallonsUsed = float(input("Enter gallons of gas used:\t"))
CostPerGallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = round((milesDriven / gallonsUsed),1)
ttlGasCost = round(gallonsUsed * CostPerGallon, 1)
costPerMile = round(ttlGasCost / milesDriven, 1)
            
# format and display the result
print()
print("Miles Per Gallon:\t", mpg,
      "\nTotal Gas Cost:\t\t", ttlGasCost,
      "\nCost Per Mile:\t\t", costPerMile)
print()
print("Bye")


