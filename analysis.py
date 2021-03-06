import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters'] / 100) ** 2)
print(bmi)

# manual slicing
'''
input_list = sorted(df['BMI'], reverse=False)
print(input_list)
severeThinness = []
print(len(severeThinness), severeThinness)
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
print(len(obeseClass_II), obeseClass_II)'''

# using filter and lambda functions
'''print(list(filter(lambda b: b < 16.9, bmi)))
print(list(filter(lambda b: 17 < b < 18.4, bmi)))
print(list(filter(lambda b: 18.5 < b < 24.9, bmi)))
print(list(filter(lambda b: 25 < b < 29.9, bmi)))
print(list(filter(lambda b: 30 < b < 34.9, bmi)))
print((list(filter(lambda b: 35 < b < 39.9, bmi))))
print((list(filter(lambda b: 40 < b < 49.9, bmi))))
print((list(filter(lambda b: b > 50, bmi))))'''

# nem variables
severeThinness = (list(filter(lambda b: b < 16.9, bmi)))
moderateThinness = (list(filter(lambda b: 17 < b < 18.4, bmi)))
mildThinness = (list(filter(lambda b: 18.5 < b < 24.9, bmi)))
normal = (list(filter(lambda b: 25 < b < 29.9, bmi)))
overweight = (list(filter(lambda b: 30 < b < 34.9, bmi)))
obeseClassI = (list(filter(lambda b: 35 < b < 39.9, bmi)))
obeseClassII = (list(filter(lambda b: 40 < b < 49.9, bmi)))
obeseClassIII = (list(filter(lambda b: b > 50, bmi)))
# variables length
print('Severe Thinness:  ', len(severeThinness), severeThinness)
print('Moderate Thinness:', len(moderateThinness), moderateThinness)
print('Mild Thinness:   ', len(mildThinness), mildThinness)
print('Normal:          ', len(normal), normal)
print('Overweight:      ', len(overweight), overweight)
print('Obese Class I:   ', len(obeseClassI), obeseClassI)
print('Obese Class II:  ', len(obeseClassII), obeseClassII)
print('Obese Class III: ', len(obeseClassIII), obeseClassIII)
print(len(severeThinness), len(moderateThinness), len(mildThinness), len(normal), len(overweight),
      len(obeseClassI), len(obeseClassII), len(obeseClassIII))
# data for a pie plot
bmiNames = ['Severe Thinness', 'Moderate Thinness', 'Mild Thinness', 'Normal', 'Overweight', 'Obese Class I',
            'Obese Clas II', 'Obese Class III']
bmirange = [0, 2, 32, 29, 18, 11, 3, 0]

# pie plot
fig = plt.figure(figsize=(10, 7))
plt.pie(bmirange, labels=bmiNames)
plt.show()

# gender proportion
gender = df['Gender']
female = (list(filter(lambda a: a == 'female', gender)))
print('Female', len(female), '%')
male = list(filter(lambda a: a == 'male', gender))
print('Male', len(male), '%')
