print("This program takes your age and tells you how much life is remaining")
#Asking for age and converting it to type int
age = int(input("What is your current age?"))
#calculating remaining years based on expected 90
remainingYears = 90-age
#calculating remaining values based on remaining years
remainingDays = remainingYears*365
remainingWeeks = remainingYears*52
remainingMonths = remainingYears * 12
# Outputting the result
print(f"You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left")