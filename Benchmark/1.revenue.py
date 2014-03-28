import MySQLdb
from datetime import datetime, timedelta
import time
from progressbar import *
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="tms")
cursor = db.cursor()

transp={'bus':0,'subway':1,'train':2}
trips = [0,0,0]

with open('revenue.loc','w') as f:
	pbar=ProgressBar().start()
	for i in range(0,100000):
		pbar.update(i/1000)
		#print '\r'+str(i+1),
		temp = [0,0,0]
		date = 0

		duration = time.time()
		cursor.execute('SELECT v_date, v_company FROM validations WHERE v_t_id = '+str(i+1)+' ORDER BY 1;')
		f.write(str(i+1)+' '+str(time.time() - duration)+'\n')
		for row in cursor.fetchall():
			if date != 0:
				if row[0] - date < timedelta(0, 7200):
					temp[transp[row[1]]] += 1
				else:
					for j in range(3):
						trips[j] += 1.0 * temp[j] / sum(temp)
					temp = [0,0,0]
					date = row[0]
					temp[transp[row[1]]] += 1
			else:
				date = row[0]
				temp[transp[row[1]]] += 1

		if sum(temp) > 0:
			for j in range(3):
				trips[j] += 1.0 * temp[j] / sum(temp)

	f.write('\n##### REVENUE COMPUTATION #####\n')
	if sum(trips) > 0:
		f.write('   Bus Company: ' + str(round(100.0*trips[0]/sum(trips),2)) + ' %\n')
		f.write('Subway Company: ' + str(round(100.0*trips[1]/sum(trips),2)) + ' %\n')
		f.write(' Train Company: ' + str(round(100.0*trips[2]/sum(trips),2)) + ' %\n')
	else:
		f.write('   Bus Company: 0%\n')
		f.write('Subway Company: 0%\n')
		f.write(' Train Company: 0%\n')
	pbar.finish()
