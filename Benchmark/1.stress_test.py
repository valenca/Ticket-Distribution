from multiprocessing import Process
import gzip
import time
import MySQLdb

def val(v_id):
	i = 0
	db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="tms")
	cursor = db.cursor()
	with gzip.open('Validations/val_'+v_id+'.gz.db', 'rb') as f:
		with open('Validations/time_'+v_id+'.loc','w') as g:
			for line in f:
				i += 1
				duration = time.time()
				cursor.execute(line)
				db.commit()
				g.write(str(time.time() - duration)+'\n')
				print 'Val_'+v_id+": "+str(i)

def dep(d_id):
	i = 0
	db = MySQLdb.connect(host="localhost",user="root",passwd="password",db="tms")
	cursor = db.cursor()
	with gzip.open('Deposits/dep_'+str(d_id)+'.gz.db', 'rb') as f:
		with open('Deposits/time_'+d_id+'.loc','w') as g:
			for line in f:
				i += 1
				duration = time.time()
				cursor.execute(line)
				db.commit()
				g.write(str(time.time() - duration)+'\n')
				if i % 1000 == 0:
					print 'Dep_'+d_id+": "+str(i)
				

validations = [Process(target=val, args=(str(i),)) for i in range(10)]
#deposits = [Process(target=dep, args=(str(i),)) for i in range(10)]

[i.start() for i in validations]
#[i.start() for i in deposits]

[i.join() for i in validations]
#[i.join() for i in deposits]
