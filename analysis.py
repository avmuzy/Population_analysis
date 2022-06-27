import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters'] / 100) ** 2)
print(bmi)