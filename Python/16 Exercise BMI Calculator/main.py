print("This program takes your height and weight as input and calculates the BMI")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/(height**2))
print(f"Your BMI is {bmi}")