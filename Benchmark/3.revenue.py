import MySQLdb
from datetime import datetime, timedelta

db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="tms")
cursor = db.cursor()

transp={'bus':0,'subway':1,'train':2}
trips = [0,0,0]

for i in range(0,5):
	print i+1
	temp = [0,0,0]
	date = 0

	cursor.execute('SELECT v_date, v_company FROM validations WHERE v_t_id = '+str(i+1)+' ORDER BY 1;')
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

print '##### REVENUE COMPUTATION #####'
if sum(trips) > 0:
	print '   Bus Company: ' + str(round(100.0*trips[0]/sum(trips),2)) + " %"
	print 'Subway Company: ' + str(round(100.0*trips[1]/sum(trips),2)) + " %"
	print ' Train Company: ' + str(round(100.0*trips[2]/sum(trips),2)) + " %"
else:
	print '   Bus Company: 0%'
	print 'Subway Company: 0%'
	print ' Train Company: 0%'
