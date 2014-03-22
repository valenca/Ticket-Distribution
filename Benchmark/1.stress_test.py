from threading import Thread
from datetime import datetime, timedelta
from random import seed, randint, choice, gauss, random
#from MySQLdb import connect
from time import time
from cPickle import dump

seed('SGD')
'''
# x - threads - 2
# y - runs - 100.000
# z - interval - [1,1000]
# x * y = 10.000.000
# y * z = 100.000.000

class Deposits(Thread):

	def __init__(self,num):
		Thread.__init__(self)
		self.num = num

	def run(self):
		values = []
		db = connect(host="localhost",user="root",passwd="password",db="tms")
		cursor = db.cursor()
		date = datetime(2004,9,1,0,0,0)
		for y in range(100000):

			date += timedelta(seconds=randint(1,1000))
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
			#print string

			duration = time()
			cursor.execute(string)
			db.commit()
			duration = time()-duration
			print duration

			values.append([y, duration])

		with open('Deposits/results'+str(self.num), "w") as f:
			dump(values,f)

# x - threads - 2
# y - runs - 1000
# z - interval - [0-2]
# b - block - 50000
# x * y * b = 100.000.000
# y * z * b = 864.000
'''
class Validations(Thread):

	def __init__(self,num):
		Thread.__init__(self)
		self.num = num

	def run(self):
		values = []
		#db = connect(host="localhost",user="root",passwd="password",db="tms")
		#cursor = db.cursor()
		date = datetime(2004,10,1,0,0,0)
		for y in range(1):
			string = 'INSERT INTO validations (v_t_id,v_date,v_location,v_transport,v_company) VALUES '
			for b in range(50000):

				date += timedelta(seconds=choice([0,0,0,1]))
				t_id = 0
				while not 0<t_id<1000001:
					t_id = int(round(gauss(5000000,2500000)))
				transp = random()
				if transp < 0.1: transp = 'train'
				elif transp < 0.5: transp = 'bus'
				else: transp = 'subway'

				string+= '('+str(t_id)+','
				string+= '\''+str(date)+'\','
				string+= '\''+transp+'_stop_'+str(randint(1,100))+'\','
				string+= '\''+transp+'_'+str(randint(1,100))+'\','
				string+= '\''+transp+'\')'
				if b != 10000-1: string+= ','
			string += ';'
			#print string

			#duration = time()
			#cursor.execute(string)
			#db.commit()
			#duration = time()-duration
			#print duration

			#values.append([y, duration])

		#with open('Validations/results'+str(self.num), "w") as f:
		#	dump(values,f)

validations = [Validations(i+1) for i in range(1)]
[i.start() for i in validations]

#deposits = [Deposits(i+1) for i in range(2)]
#[i.start() for i in deposits]
