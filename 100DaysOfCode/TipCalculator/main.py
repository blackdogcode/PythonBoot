print("Welcome to the tip calculator!")

print("What was the bill?")
bill = float(input("$"))

print("What percentage tip would you like to give? e.g 10%, 15%, 20%")
tip_percent = float(input()[:-1])

print("How many people to split the bill?")
num_people = int(input())

total_bill = bill * (1 + tip_percent / 100)
each_person_pay = total_bill / num_people
print(f"Each person should pay: ${round(each_person_pay, 2)}")
