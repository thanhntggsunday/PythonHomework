pdk = 0.45359237
idm = 0.0254
b = False
while (not b):
    try:
        weight = float(input('Weight in pounds: '))
        b = True
    except:
        print('You input wrong data type. try again')

b = False
while (not b):
    try:
        height = float(input('Height in inches: '))
        b = True
    except:
        print('You input wrong data type. try again')

bmi = weight * pdk / (height * idm) ** 2
print("BMI = ", bmi)

if bmi < 18.5:
    print("Body is Underweight")
elif bmi < 25:
    print("Body is Normal")
elif bmi < 30:
    print("Body is Overweight")
else:
    print("Body is Obese")
