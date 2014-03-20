from random import randint,choice,gauss
from sys import stdout as out
from util import bar
import datetime


start_date = datetime.datetime(2010,1,1,0,0,0)

if True:
	with open('Data/deposits.db','w') as f:
		tot=5000000
		for i in range(tot):
			
			bar(i,tot)

			current_date = start_date + datetime.timedelta(seconds=randint(1,131200000))
			query="INSERT INTO tms.deposits (ticket_id,date,location,trips,value) VALUES ("

			query+= str(randint(1,3000000))+",\'"
			query+= str(current_date)+"\',"
			query+= str(choice(['\'mc','\'st'])+str(randint(1,100)))+"\',"
			t=int(round(gauss(8,4)))
			query+= str(t)+","
			query+= str(t*1.2)+");"
			f.write(query+"\n")
	print ""

if True:
	with open('Data/validations.db','w') as f:
		tot=20000000
		for i in range(tot):
			
			bar(i,tot)

			current_date = start_date + datetime.timedelta(seconds=randint(1,131200000))
			query="INSERT INTO tms.validations (ticket_id,date,location,transport) VALUES ("

			query+= str(randint(1,3000000))+",\'"
			query+= str(current_date)+"\',"
			query+= str(choice(['\'trs','\'sws','\'bss'])+str(randint(1,100)))+"\',"
			query+= str(choice(['\'tr','\'sw','\'bs'])+str(randint(1,100)))+"\')"
			f.write(query+"\n")
	print ""
