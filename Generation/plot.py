import plotly
from matplotlib import pyplot
import os

py = plotly.plotly("Mehlins", "vq0aqwkoz4")

indexes_d = list(range(1,101,5))
indexes_v = list(range(1,21))

data_d1 = []
total_d1 = []
for f in [i for i in os.listdir('Deposits/') if i[:4] == 'time']:
	with open('Deposits/'+f) as g:
		data_d1.append([float(g.readline()) for j in range(100)])
		total_d1.append(float(g.readline()))
data_d1 = [float(sum(l))/len(l) for l in zip(*data_d1)]
data_d1 = [sum(data_d1[j*5:(j+1)*5])/5 for j in range(20)]

data_d2 = []
total_d2 = []
for f in [i for i in os.listdir('Deposits2/') if i[:4] == 'time']:
	with open('Deposits2/'+f) as g:
		data_d2.append([float(g.readline()) for j in range(100)])
		total_d2.append(float(g.readline()))
data_d2 = [float(sum(l))/len(l) for l in zip(*data_d2)]
data_d2 = [sum(data_d2[j*5:(j+1)*5])/5 for j in range(20)]

data_v1 = []
total_v1 = []
for f in [i for i in os.listdir('Validations/') if i[:4] == 'time']:
	with open('Validations/'+f) as g:
		data_v1.append([float(g.readline()) for j in range(20)])
		total_v1.append(float(g.readline()))
data_v1 = [float(sum(l))/len(l) for l in zip(*data_v1)]

data_v2 = []
total_v2 = []
for f in [i for i in os.listdir('Validations2/') if i[:4] == 'time']:
	with open('Validations2/'+f) as g:
		data_v2.append([float(g.readline()) for j in range(20)])
		total_v2.append(float(g.readline()))
data_v2 = [float(sum(l))/len(l) for l in zip(*data_v2)]


trace0 = {'x': indexes_d,
  'y': data_d1}

trace1 = {'x': indexes_d,
  'y': data_d2}

trace2 = {'x': indexes_v,
  'y': data_v1}

trace3 = {'x': indexes_v,
  'y': data_v2}

py.plot([trace0, trace1])
py.plot([trace2, trace3])


