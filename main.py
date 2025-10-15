print("BMI Checker")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
 
bmi = weight / (height ** 2)
print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
    print("UNDERWEIGHT (<18.5)")
elif 18.5 <= bmi <= 24.9:
    print("NORMAL (18.5-24.9)")
elif 25 <= bmi <= 29.9:
    print("OVERWEIGHT (25-29.9)")
elif 30 <= bmi <= 34.9:
    print("OBESE (30-34.9)")
else:
    print("EXTREMELY OBSES (≥35)")
