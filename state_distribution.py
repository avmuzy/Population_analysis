import pandas as pd
import matplotlib.pyplot as plt
import statistics
from functools import reduce

# reading csv file
x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)

# setting target column
stateFull = df['StateFull']

# Setting states as variables
ac = list(filter(lambda b: b == 'Acre', stateFull))
al = list(filter(lambda b: b == 'Alagoas', stateFull))
ap = list(filter(lambda b: b == 'Amapá', stateFull))
am = list(filter(lambda b: b == 'Amazonas', stateFull))
ba = list(filter(lambda b: b == 'Bahia', stateFull))
ce = list(filter(lambda b: b == 'Ceará', stateFull))
df = list(filter(lambda b: b == 'Distrito Federal', stateFull))
es = list(filter(lambda b: b == 'Espirito Santo', stateFull))
go = list(filter(lambda b: b == 'Goiás ', stateFull))
ma = list(filter(lambda b: b == 'Maranhão ', stateFull))
mt = list(filter(lambda b: b == 'Mato Grosso ', stateFull))
ms = list(filter(lambda b: b == 'Mato Grosso do Sul ', stateFull))
mg = list(filter(lambda b: b == 'Minas Gerais ', stateFull))
pa = list(filter(lambda b: b == 'Pará ', stateFull))
pb = list(filter(lambda b: b == 'Paraíba ', stateFull))
pr = list(filter(lambda b: b == 'Paraná', stateFull))
pe = list(filter(lambda b: b == 'Pernambuco', stateFull))
pi = list(filter(lambda b: b == 'Piauí', stateFull))
rj = list(filter(lambda b: b == 'Rio de janeiro', stateFull))
rn = list(filter(lambda b: b == 'Rio Grande do Norte ', stateFull))
rs = list(filter(lambda b: b == 'Rio Grande do Sul', stateFull))
ro = list(filter(lambda b: b == 'Rondônia', stateFull))
rr = list(filter(lambda b: b == 'Roraima', stateFull))
sc = list(filter(lambda b: b == 'Santa Catarina', stateFull))
sp = list(filter(lambda b: b == 'São Paulo', stateFull))
se = list(filter(lambda b: b == 'Sergipe', stateFull))
to = list(filter(lambda b: b == 'Tocantins', stateFull))
