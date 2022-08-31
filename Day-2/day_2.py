# Tip calculator

print("Welcome to tip calculator.")
total_bill = float(input("What was the total bill?: $"))
split = float(input("How many people to split the bill?: "))
tip = float(input("What percentage tip would you like to give?: "))

each_person = (total_bill + (total_bill * (tip/100))) / split
print(f"Each person should pay ${each_person:.2f}")
