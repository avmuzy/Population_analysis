import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('new_data_base.csv')
df = pd.DataFrame(x)
print(x)
age = df["Age"]
kilo = df['Kilograms']
bmix = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)
fig, ax = plt.subplots()
ax.plot(age, bmix)

ax.set(xlabel='Age', ylabel='BMI',
       title='Age X BMI')
ax.grid()

fig.savefig("test1.png")
plt.show()
plt.stem(age, bmix)
plt.show()