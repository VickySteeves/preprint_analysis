import sys
import matplotlib.pyplot as plt

logFile = sys.argv[1]
arxiv = sys.argv[2]

# open the log file
lf = open(logFile, "r")

# read the file line by line
delays = []
for line in lf:
  d = int(line)
  if (d >= 0):
    delays.append( d ) 

# close the log file
lf.close()

# make the histogram
binwidth = 30 # data is in days
b = range( min(delays), max(delays) + binwidth, binwidth )
plt.hist(delays, bins=b)
plt.ylabel('Number of Papers')
plt.xlabel('Delay (Days)')
plt.title(arxiv)
#plt.yscale('log', nonposy='clip')
plt.show()
