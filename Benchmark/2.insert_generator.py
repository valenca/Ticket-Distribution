from random import randint,choice,gauss,seed
from sys import stdout as out
from util import bar
import datetime
seed('sgd')

start_date = datetime.datetime(2014,1,1,0,0,0)
tickets = 10

if True:
	with open('Data/deposits.db','w') as f:
		tot=50
		for i in range(tot):
			t=int(round(gauss(8,4)))
			bar(i,tot,msg="deposit")
			current_date = start_date + datetime.timedelta(seconds=randint(1,86400))
			f.write("INSERT INTO tms.deposits (ticket_id,date,location,trips,value) VALUES (")
			f.write(str(randint(1,tickets))+",\'"+str(current_date)+"\',")
			f.write(str(choice(['\'mc','\'st'])+str(randint(1,100)))+"\',")
			f.write(str(t)+","+str(t*1.2)+");\n")

if True:
	with open('Data/validations.db','w') as f:
		tot=200
		for i in range(tot):
			t=choice(['tr','sw','bs'])
			bar(i,tot,msg="validation")
			current_date = start_date + datetime.timedelta(seconds=randint(1,86400))
			f.write("INSERT INTO tms.validations (ticket_id,date,location,transport) VALUES (")
			f.write(str(randint(1,tickets))+",\'"+str(current_date)+"\',")
			f.write('\'s'+t+str(randint(1,100))+"\',")
			f.write('\''+t+str(randint(1,100))+"\');\n")
