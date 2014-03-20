from sys import stdout as out
from math import floor,ceil

def bar(i,tot,length=40):
	pcurr=length*(i)/tot
	clean="\r"
	if i<tot-1:
		bar="["+("#"*int(ceil(pcurr)))+("-"*int(floor(length-pcurr-1)))+"]"
		perc=" ("+str(i+1)+"/"+str(tot)+") "
		out.write(clean+bar+perc)
	else:
		bar="["+("#"*int(ceil(pcurr)))+"]"
		perc=" ("+str(i+1)+"/"+str(tot)+")\n"
		out.write(clean+bar+perc)
		out.flush()
