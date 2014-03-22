from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
from multiprocessing import Process, Queue
import sys
import time

from MySQLdb import connect

def f(v_queries):
	date = datetime(2004,10,1,0,0,0)
	for y in range(3):
		string = 'INSERT INTO validations (v_t_id,v_date,v_location,v_transport,v_company) VALUES '
		x = 10000
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
		v_queries.put(string)


if __name__ == '__main__':

	db = connect(host="localhost",user="root",passwd="password",db="tms")
	cursor = db.cursor()

	v_queries = Queue()
	validations = [Process(target=f, args=(v_queries,)) for i in range(6)]
	[i.start() for i in validations]

	times1 = time.time()
	x = 0
	while x < 18:
		a = v_queries.get()
		if x == 17:
			duration = time.time()
			cursor.execute(a)
			db.commit()
			duration = time.time()-duration
			print 'a',duration
		times2 = time.time()
		print times2-times1
		times1 = times2
		x += 1

	[i.join() for i in validations]
