import datetime
import random
from string import letters

with open('firstnames','r') as f:
	firstnames = [line[:-1] for line in f]
with open('lastnames','r') as f:
	lastnames = [line[:-1] for line in f]

firstnames = list(set(firstnames))
lastnames = list(set(lastnames))

with open('Data/tickets_data','w') as f:

	start_date = datetime.datetime(2000,1,1,0,0,0)
	end_date = datetime.datetime(2014,2,28,23,59,59)

	num = 0
	current_date = start_date + datetime.timedelta(seconds=random.randint(1,290))
	while current_date <= end_date:
		balance = int(round(random.gauss(8,4)))
		if balance < 0: balance = 0
		f.write(str(num+1)+'|'+str(random.choice([0,1]))+'|')
		f.write(random.choice(firstnames)+' '+random.choice(firstnames)+' '+random.choice(lastnames)+' '+random.choice(lastnames)+'|')
		f.write(str(current_date)+'|'+str(random.randint(1,1000))+'|'+str(balance)+'|')
		f.write("".join([random.choice(letters) for i in range(200)])+"\n")
		current_date += datetime.timedelta(seconds=random.randint(1,290))
		num+=1
		print num

	print num