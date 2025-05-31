import matplotlib.pyplot as plt
import numpy as np

with open('population.csv', encoding="utf-8") as data:
    read_data = data.read()

read_data = read_data.split('\n')
header = read_data[0]
body = read_data[1:]

year = []
ac_pop = []

for item in body:
    item = item.split(',')
    year.append(int(item[0]))
    ac_pop.append(int(item[1]))

time = np.array(year)
population = np.array(ac_pop)

fig, ax = plt.subplots()

ax.plot(time, population)
ax.set(xlabel='time (year)', 
       ylabel='population (millions of persons)', 
       title='Census Population of Allegheny County')
ax.grid()
plt.show()
