from datetime import datetime, timedelta
from random import seed, randint, choice, gauss

seed('SGD')
date = datetime(2000,1,1,0,0,0)
with open('firstnames','r') as f: firstnames = list(set([line[:-1] for line in f]))
with open('lastnames','r') as f: lastnames = list(set([line[:-1] for line in f]))
with open('tickets.db','w') as f:
	for i in range(1000000):
		date += timedelta(seconds=randint(1,290))
		balance = int(round(gauss(8,4)))
		if balance < 0: balance = 0
		string = str(i+1)+'|'
		string+= choice(['normal','normal','normal','premium'])+'|'
		string+= choice(firstnames)+' '+choice(firstnames)+' '+choice(lastnames)+' '+choice(lastnames)+'|'
		string+= str(date)+'|'
		string+= 'store_'+str(randint(1,100))+'|'
		string+= str(balance)+'\n'
		f.write(string)
		#print "\r"+str(i+1),
