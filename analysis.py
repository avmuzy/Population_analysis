import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters'] / 100) ** 2)
print(bmi)
input_list = sorted(df['BMI'], reverse=False)
print(input_list)
severeThinness = [0]

moderateThinness = input_list[:2]
print(len(moderateThinness), moderateThinness)
mildThinness = input_list[3:37]
print(len(mildThinness), mildThinness)
normal = input_list[38:66]
print(len(normal), normal)
overweight = input_list[67:84]
print(len(overweight), overweight)
obeseClass_I = input_list[85:96]
print(len(obeseClass_I), obeseClass_I)
obeseClass_II = input_list[97:99]
print(len(obeseClass_II), obeseClass_II)

