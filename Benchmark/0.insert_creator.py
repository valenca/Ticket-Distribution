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

if __name__ == '__main__':

	validations = [Process(target=create_val, args=(i,)) for i in range(5)]
	[i.start() for i in validations]
	[i.join() for i in validations]
