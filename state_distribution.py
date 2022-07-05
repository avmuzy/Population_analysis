import pandas as pd
import matplotlib.pyplot as plt
import statistics
from functools import reduce

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
print(x)