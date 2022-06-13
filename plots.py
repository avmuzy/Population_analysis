import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('new_data_base.csv')
df = pd.DataFrame(x)
print(x)

fig, ax = plt.subplots()
ax.plot(['Age'], ['Kilograms'])

ax.set(xlabel='Age', ylabel='Kilograms',
       title='Age X kilograms')
ax.grid()

fig.savefig("test1.png")
plt.show()
