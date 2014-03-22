from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
import sys
import time
import marshal as cPickle
import gzip

queries=[]
date = datetime(2004,10,1,0,0,0)
for y in range(2):
	string = 'INSERT INTO validations (v_t_id,v_date,v_location,v_transport,v_company) VALUES '
	x = 10
	for b in range(x):

		date += timedelta(seconds=choice([0,0,0,1]))
		t_id = 0
		while not 0 < t_id < 1000001:
			t_id = int(round(gauss(5000000,2500000)))
		transp = choice(['train','bus','bus','bus','bus','subway','subway','subway','subway','subway'])

		string+= '('+str(t_id)+','
		string+= '\''+str(date)+'\','
		string+= '\''+transp+'_stop_'+str(randint(1,100))+'\','
		string+= '\''+transp+'_'+str(randint(1,100))+'\','
		string+= '\''+transp+'\')'
		if b != x-1: string+= ','

	string += ';'
	queries.append(string)

a = time.time()
#with open('tester','w') as f:
	#[f.write(string+'\n') for string in queries]
	#cPickle.dump(queries,f)
with gzip.open('file.txt.gz.db', 'wb') as f:
	[f.write(string+'\n') for string in queries]
print time.time()-a
queries = []
with gzip.open('file.txt.gz.db', 'rb') as f:
	queries = [line for line in f.read().split('\n')]
	queries.pop()
	print queries
