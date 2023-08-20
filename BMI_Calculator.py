#BMI 2.0
#problem
'''Calculate BMI of user '''

# Solution


print("*** Welcome to BMI Calculator ***\n")

#Asking user to enter the details
height = float(input("Enter your height in m: "))
print()
weight = float(input("Enter your weight in kg: "))

BMI =round(weight/height ** 2)

print()
# Result
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI> 18.5 and BMI<=25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI> 25 and BMI <=30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI> 30 and BMI <=35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

print()
print("*** Thank you ***")