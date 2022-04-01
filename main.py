print("Enter your weight in kg")
weight=float(input())
print("Enter your height in m")
height=float(input())
bmi=round(weight/height**2)
if bmi<35:
  if bmi>=30:
    print(f"Your BMI is {bmi} you are obese")
  elif bmi>=25:
     print(f"Your BMI is {bmi} you are slightly overweight")
  elif bmi<=18.5:
    print(f"Your BMI is {bmi} you are underweight")
  else:
    print(f"Your BMI is {bmi} you have normal weight")
else:
 print(f"Your BMI is {bmi} you are clinically obese.")

  
  
        







