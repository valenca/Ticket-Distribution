from multiprocessing import Process
import gzip
import time
import MySQLdb

def val(v_id):
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="tms")
	cursor = db.cursor()
	n=str(v_id)
	i=0
	with gzip.open('Validations/val_'+n+'.gz.db', 'rb') as f:
		with open('valtime'+n+'.db','w') as g:
			for line in f:
				duration = time.time()
				cursor.execute(line)
				db.commit()
				g.write(time.time() - duration)
				print "V",i
				i+=1

def dep(d_id):
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="tms")
	cursor = db.cursor()
	n=str(d_id)
	i=0
	with gzip.open('Deposits/dep_'+n+'.gz.db', 'rb') as f:
		with open('deptime'+n+'.db','w') as g:
			for line in f:
				duration = time.time()
				cursor.execute(line)
				db.commit()
				g.write(time.time() - duration)
				print "D",i
				i+=1

validations = [Process(target=val, args=(i,)) for i in range(10)]
deposits = [Process(target=dep, args=(i,)) for i in range(10)]

[i.start() for i in validations]
[i.start() for i in deposits]

[i.join() for i in validations]
[i.join() for i in deposits]
