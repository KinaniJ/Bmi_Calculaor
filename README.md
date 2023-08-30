# Bmi_Calculaor
It first inputs the weight(kg) and height(meters) of a person
  weight = float(input("what is your weight in KG"))
  height = float(input("what is your Height in meters"))
the funcion then calculates the Bmi of a person by diving the weight with the square of the height
  def bmi(*b):
      b = weight / (height * 2)
      return b
the if statement is used to determine the weight category
  if Bmi < 18.5:
      print('Under Weight')
  elif Bmi == "18.5" and b > 25:
      print("Normal weight")
  elif Bmi >= 25 and b <=29.9:
      print('Over Weight')
  else:
      print('obese')
