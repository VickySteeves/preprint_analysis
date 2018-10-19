import os
import sys

dir = sys.argv[1]
keyword = sys.argv[2]

years = ['2017', '2018']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

results = []
for year in years:
  for month in months:
     file = dir + 'eartharxiv_keyword_counts_' + year + '_' + month + '.log'
     if os.path.isfile(file):
       fh = open(file, "r")
       for line in fh:
         parts = line.split(",")
         count = parts[0].strip()
         key = parts[1].strip()
         if (key == keyword):
           results.append(str(count).strip())
           break
       fh.close()
     else:
       results.append('0')

for i in results:
  print(i)
