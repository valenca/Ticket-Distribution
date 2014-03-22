from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
from multiprocessing import Process
import gzip

# x - threads - 10
# y - runs - 200
# z - interval - [0,0,0,1]
# b - block - 50000
# x * y * b = 100.000.000
def create_val(v_id):
	queries=[]
	date = datetime(2004,10,1,0,0,0)
	for y in range(200):
		string = 'INSERT INTO validations (v_t_id,v_date,v_location,v_transport,v_company) VALUES '
		x = 50000
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
		print str(v_id),str(y)

	with gzip.open('Validations/val_'+str(v_id)+'.gz.db', 'wb') as f:
		[f.write(string+'\n') for string in queries]


# x - threads - 10
# y - runs - 1.000.000
# z - interval - [1,100]
# x * y = 10.000.000
# y * z = 100.000.000
def create_dep(d_id):
	queries=[]
	date = datetime(2004,9,1,0,0,0)
	for y in range(1000000):

		date += timedelta(seconds=randint(1,100))
		t_id = 0
		while not 0<t_id<1000001:
			t_id = int(round(gauss(5000000,2500000)))
		trips = int(round(gauss(8,4)))
		if trips < 1: trips = 1

		string = 'INSERT INTO deposits (d_t_id,d_date,d_location,d_trips,d_value) VALUES ('
		string+= str(t_id)+','
		string+= '\''+str(date)+'\','
		string+= '\''+str(choice(['machine','store'])+'_'+str(randint(1,100)))+'\','
		string+= str(trips)+','
		string+= str(trips*1.2)+');'

		queries.append(string)
		if y%10000 == 0: print str(d_id),str(y)

	with gzip.open('Deposits/dep_'+str(d_id)+'.gz.db', 'wb') as f:
		[f.write(string+'\n') for string in queries]


if __name__ == '__main__':

	#validations = [Process(target=create_val, args=(i+10,)) for i in range(5)]
	#[i.start() for i in validations]
	#[i.join() for i in validations]

	#deposits = [Process(target=create_dep, args=(i+10,)) for i in range(5)]
	#[i.start() for i in deposits]
	#[i.join() for i in deposits]
