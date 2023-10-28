weight = int(input("Type your weight in KG: "))
height = float(input ("Type your height in Inches: "))

BMI = (weight * 703) / (height * height)

print (BMI)

if BMI <= 18.5 :
    print("You're underweight")
elif BMI <= 25:
    print ("You're normal")
elif BMI <= 30:
    print ("You're Over weight")
elif BMI <= 40:
    print ("You're Obese")
else:
    print ("you have fallen")