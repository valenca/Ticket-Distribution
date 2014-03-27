from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
from multiprocessing import Process
import gzip

# x - threads - 10
# y - runs - 20
# z - interval - [0,0,0,1]
# b - block - 50000
# x * y * b = 10.000.000
def create_val(v_id):
	queries=[]
	date = datetime(2004,10,1,0,0,0)
	for y in range(20):
		string = 'INSERT INTO validations (v_t_id,v_date,v_location,v_transport,v_company) VALUES '
		x = 50000
		for b in range(x):

			date += timedelta(seconds=choice([0,0,0,1]))
			t_id = 0
			while not 0 < t_id < 100001:
				t_id = int(round(gauss(50000,25000)))
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
# y - runs - 20
# z - interval - [1,1000]
# b - block - 5000
# x * y * b = 1.000.000
# y * z * b = 100.000.000
def create_dep(d_id):
	queries=[]
	date = datetime(2004,9,1,0,0,0)
	for y in range(20):
		string = 'INSERT INTO deposits (d_t_id,d_date,d_location,d_trips,d_value) VALUES '
		x = 5000
		for b in range(x):

			date += timedelta(seconds=randint(1,1000))
			t_id = 0
			while not 0<t_id<100001:
				t_id = int(round(gauss(50000,25000)))
			trips = int(round(gauss(10,5)))
			if trips < 1: trips = 1

			string+= '('+str(t_id)+','
			string+= '\''+str(date)+'\','
			string+= '\''+str(choice(['machine','store'])+'_'+str(randint(1,100)))+'\','
			string+= str(trips)+','
			string+= str(trips*1.2)+')'
			if b != x-1: string+= ','

		string += ';'
		queries.append(string)
		print str(d_id),str(y)

	with gzip.open('Deposits/dep_'+str(d_id)+'.gz.db', 'wb') as f:
		[f.write(string+'\n') for string in queries]


if __name__ == '__main__':

	validations = [Process(target=create_val, args=(i,)) for i in range(10)]
	[i.start() for i in validations]
	[i.join() for i in validations]

	deposits = [Process(target=create_dep, args=(i,)) for i in range(10)]
	[i.start() for i in deposits]
	[i.join() for i in deposits]
