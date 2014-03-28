from multiprocessing import Process
import gzip
import time
import MySQLdb

def val(v_id):
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="tms")
	cursor = db.cursor()
	with gzip.open('Validations/val_'+str(v_id)+'.gz.db', 'rb') as f:
		for line in f:
			duration = time.time()
			cursor.execute(line)
			db.commit()
			print time.time() - duration

def dep(d_id):
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="tms")
	cursor = db.cursor()
	with gzip.open('Deposits/dep_'+str(d_id)+'.gz.db', 'rb') as f:
		for line in f:
			duration = time.time()
			cursor.execute(line)
			db.commit()
			print time.time() - duration

validations = [Process(target=val, args=(i,)) for i in range(10)]
#deposits = [Process(target=dep, args=(i,)) for i in range(10)]

[i.start() for i in validations]
#[i.start() for i in deposits]

[i.join() for i in validations]
#[i.join() for i in deposits]
