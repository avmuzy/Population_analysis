# simple BMI calculation

height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kilograms: '))
bmi = weight / height**2
print('Tour BMI is: %4f' % bmi)

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

