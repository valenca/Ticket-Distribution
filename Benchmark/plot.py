import plotly
from matplotlib import pyplot
import os

py = plotly.plotly("Mehlins", "vq0aqwkoz4")

with open('revenue.loc') as f:
	data1 = [float(f.readline().split()[1]) for i in range(100000)]
data1.sort()
data1 = [sum(data1[j*1000:(j+1)*1000])/1000 for j in range(100)]

with open('revenue2.loc') as f:
	data2 = [float(f.readline().split()[1]) for i in range(100000)]
data2.sort()
data2 = [sum(data2[j*1000:(j+1)*1000])/1000 for j in range(100)]

box1 = {'y': data1,
  	'type': 'box',
  	'boxpoints': 'all',
  	'jitter': 0.1,
  	'pointpos': -1.2}

box2 = {'y': data2,
  	'type': 'box',
  	'boxpoints': 'all',
  	'jitter': 0.1,
  	'pointpos': -1.2}

py.plot([box1,box2])


