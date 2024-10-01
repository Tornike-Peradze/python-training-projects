# Project 2: Tip Calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
given_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_amount_splitting = int(input('How many people to split the bill? '))

bill_after_tip = total_bill * (1 + (given_tip/100))

bill_to_each_person = bill_after_tip / people_amount_splitting
rounded_bill_to_each_person = round(bill_to_each_person, 2)

print(f"Each person should pay: ${rounded_bill_to_each_person}")