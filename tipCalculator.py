print("Welcome to the tip calculator. ")
totalBill = input("What was the total bill? $")
tipPercent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

newTip = int(tipPercent) / 100 + 1
billWithTip = float(totalBill) * newTip
finalPayment = round(billWithTip / int(people), 2)

print(f"Each Person should pay: ${finalPayment}")