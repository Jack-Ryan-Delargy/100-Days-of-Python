print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_percent = (tip / 100) + 1
people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${(float(bill/people))*tip_percent}",2)

