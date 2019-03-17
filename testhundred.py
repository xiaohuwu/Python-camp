#!/usr/bin/env python3
amount = float(input("Enter amout"))
inrate = float(input("Enter Inteerst rate :"))
value = 0
year = 1
while year <= 5:
    value = amount + (inrate * amount)
    print("Year {} Rs.  {:.2f} ".format(year, value))
    amount = value
    year = year + 1
