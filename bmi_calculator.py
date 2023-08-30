weight = float(input("what is your weight in KG"))
height = float(input("what is your Height in meters"))


def bmi(*b):
    b = weight / (height * 2)
    return b

Bmi = bmi(weight, height)
if Bmi < 18.5:
    print('Under Weight')
elif Bmi == "18.5" and b > 25:
    print("Normal weight")
elif Bmi >= 25 and b <=29.9:
    print('Over Weight')
else:
    print('obese')
