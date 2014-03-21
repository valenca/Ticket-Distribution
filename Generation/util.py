from sys import stdout as out
from time import sleep

def bar(i,tot,msg='',length=40):
	pcurr=length*(i)/tot
	clean="\r"
	if i<tot-1:
		bar="["+("#"*int(pcurr+1))+("-"*int(length-pcurr+1))
		perc="] ("+str(i+1)+"/"+str(tot)+") "
		out.write(clean+bar[:length]+perc+msg)
	else:
		bar="["+("#"*int(pcurr+2))
		perc="] ("+str(i+1)+"/"+str(tot)+") "
		out.write(clean+bar[:length]+perc+msg+"\n")
	out.flush()

if __name__ == "__main__":
	div=30
	for i in range(div):
		bar(i,div,msg="")
		sleep(0.05)
