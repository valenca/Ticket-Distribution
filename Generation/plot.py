import plotly
from matplotlib import pyplot
import os

py = plotly.plotly("Mehlins", "vq0aqwkoz4")

indexes = list(range(1,21))

data_d1 = []
total_d1 = []
for f in [i for i in os.listdir('Results/Standalone/Deposits/') if i[:4] == 'time']:
	with open('Results/Standalone/Deposits/'+f) as g:
		data_d1.append([float(g.readline()) for j in range(100)])
		total_d1.append(float(g.readline()))
data_d1 = [float(sum(l))/len(l) for l in zip(*data_d1)]
data_d1 = [sum(data_d1[j*5:(j+1)*5])/5 for j in range(20)]

data_d2 = []
total_d2 = []
for f in [i for i in os.listdir('Results/Standalone/Deposits2/') if i[:4] == 'time']:
	with open('Results/Standalone/Deposits2/'+f) as g:
		data_d2.append([float(g.readline()) for j in range(100)])
		total_d2.append(float(g.readline()))
data_d2 = [float(sum(l))/len(l) for l in zip(*data_d2)]
data_d2 = [sum(data_d2[j*5:(j+1)*5])/5 for j in range(20)]

data_d3 = []
total_d3 = []
for f in [i for i in os.listdir('Results/Cluster/Deposits/') if i[:4] == 'time']:
	with open('Results/Cluster/Deposits/'+f) as g:
		data_d3.append([2*float(g.readline()) for j in range(100)])
		total_d3.append(2*float(g.readline()))
data_d3 = [float(sum(l))/len(l) for l in zip(*data_d3)]
data_d3 = [sum(data_d3[j*5:(j+1)*5])/5 for j in range(20)]

data_v1 = []
total_v1 = []
for f in [i for i in os.listdir('Results/Standalone/Validations/') if i[:4] == 'time']:
	with open('Results/Standalone/Validations/'+f) as g:
		data_v1.append([float(g.readline()) for j in range(20)])
		total_v1.append(float(g.readline()))
data_v1 = [float(sum(l))/len(l) for l in zip(*data_v1)]

data_v2 = []
total_v2 = []
for f in [i for i in os.listdir('Results/Standalone/Validations2/') if i[:4] == 'time']:
	with open('Results/Standalone/Validations2/'+f) as g:
		data_v2.append([float(g.readline()) for j in range(20)])
		total_v2.append(float(g.readline()))
data_v2 = [float(sum(l))/len(l) for l in zip(*data_v2)]

data_v3 = []
total_v3 = []
for f in [i for i in os.listdir('Results/Cluster/Validations/') if i[:4] == 'time']:
	with open('Results/Cluster/Validations/'+f) as g:
		data_v3.append([5*float(g.readline()) for j in range(100)])
		total_v3.append(5*float(g.readline()))
data_v3 = [float(sum(l))/len(l) for l in zip(*data_v3)]
data_v3 = [sum(data_v3[j*5:(j+1)*5]) for j in range(20)]


trace0 = {'x': indexes,
  'y': data_d1}

trace1 = {'x': indexes,
  'y': data_d2}

trace2 = {'x': indexes,
  'y': data_d3}

trace3 = {'x': indexes,
  'y': data_v1}

trace4 = {'x': indexes,
  'y': data_v2}

trace5 = {'x': indexes,
  'y': data_v3}

py.plot([trace0, trace1])
py.plot([trace3, trace4])

py.plot([trace0, trace1, trace2])
py.plot([trace3, trace4, trace5])
