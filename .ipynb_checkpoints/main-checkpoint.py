import numpy
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)

print(x)
print(df[['Kilograms', 'Centimeters']])
print(type(x))
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)
print(bmi)