import sys
import itertools
from collections import Counter

dir = sys.argv[1]
repo1 = sys.argv[2]
repo2 = sys.argv[3]

keywords1 = []
keywords2 = [] 
repos = [repo1, repo2]

for i in range(2):
  
   file = dir + repos[i] + '/logs/' + repos[i] + '_keywords_count.log'
   f = open(file, 'r')
   for line in f:
      parts = line.split(';')
      keyword = parts[0].strip()
      count = parts[1].strip()
      k = [keyword] * int(count)
      if (i == 0):
        keywords1.extend(k)
      else:
        keywords2.extend(k)
   f.close() 

c = list(( Counter(keywords1) & Counter(keywords2) ).elements())
l1 = len(keywords1)
l2 = len(keywords2)
if ( l1 > l2 ):
  m = l2
else:
  m = l1

print("Size of " + repo1, l1)
print("Size of " + repo2, l2)
counter = Counter(c)
print("Overlap:", counter.most_common(5))
print("Min size:", m)
print("Metric:", len(c)/m)
