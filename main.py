age = int(input("What is your current age? "))

ageLeft = 90 - age

months = ageLeft * 12
weeks = ageLeft * 52
days = ageLeft * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left")
