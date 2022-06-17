# simple BMI calculation
import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmix = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)

height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kilograms: '))
bmi = weight / height**2
print('Your BMI is: %4f' % bmi)

if bmi < 16:
    print('Severe Thinness')
elif bmi < 17:
    print('Moderate Thinness')
elif bmi < 18.5:
    print('Mild Thinness')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
elif bmi < 35:
    print('Obese Class I')
elif bmi < 40:
    print('Obese Class II')
else:
    print('Obese Class III')

