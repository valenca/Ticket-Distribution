from threading import Thread
from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
#from MySQLdb import connect
#from time import time
#from cPickle import dump

global v_queries
v_queries = []

class CreateValidations(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		date = datetime(2004,10,1,0,0,0)
		for y in range(1):
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
			v_queries.append(string)

c_validations = [CreateValidations() for i in range(3)]
[i.start() for i in c_validations]
