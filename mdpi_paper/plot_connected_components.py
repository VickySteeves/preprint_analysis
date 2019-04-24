import sys
import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt

arxives = ["EartharXiv", "EngrXiv", "LawarXiv", "LISSA", "MarXiv", "MindrXiv", "PaleorXiv", "PsyarXiv", "SocarXiv"]

# directory with connected component data
directory = sys.argv[1]

# read the data
location = 1
for arxiv in arxives:

	cc_size = []
	inFile = directory + arxiv.lower() + "_cc.txt"
	f = open(inFile, "r")
	for line in f:
   		cc_size.append( int(line.strip()) )
	f.close()

	# print the largest cc size
	print(arxiv, max(cc_size) )

	# take out the largest cc, makes the plot more readable
	cc_size.remove( max(cc_size) )

 	# plotting
	binwidth = 2
	plt.subplot(3, 3, location)
	plt.hist( cc_size, bins=range(min(cc_size), max(cc_size) + binwidth, binwidth) )
	plt.title(arxiv)
	if ( (location == 1) or (location == 4) or (location == 7) ):
		plt.ylabel("# of Connected \nComponents")
	if ( (location == 7) or (location == 8) or (location == 9) ):
		plt.xlabel("# of Nodes in\n Connected Components")
	location += 1

# adjust the spacing so the title don't run into each other
# expressed as a praction of the height of each plot
plt.subplots_adjust(hspace=.9)
plt.show()