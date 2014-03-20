from random import randint,choice,gauss
from sys import stdout as out
from math import floor,ceil
import datetime

tmp=3070802

start_date = datetime.datetime(2010,1,1,0,0,0)



with open('Data/deposits_data.loc','w') as f:
	tot=500
	for i in range(tot):
		
		length=40
		pcurr=length*(i)/tot
		ptotal=length
		clean="\r"
		bar="["+("#"*int(ceil(pcurr)))+("-"*int(floor(ptotal-pcurr-1)))+"]"
		perc=" ("+str(i+1)+"/"+str(tot)+") "
		out.write(clean+bar+perc)
		out.flush()

		current_date = start_date + datetime.timedelta(seconds=randint(1,131200000))
		query="INSERT INTO tms.deposits (ticket_id,date,location,trips,value) VALUES ("

		query+= str(randint(1,tmp))+",\'"
		query+= str(current_date)+"\',"
		query+= str(choice(['\'m','\'s'])+str(randint(1,1000)))+"\',"
		t=int(round(gauss(8,4)))
		query+= str(t)+","
		query+= str(t*1.2)+");"
		f.write(query+"\n")
print ""
