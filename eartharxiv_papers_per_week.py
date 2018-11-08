import sys
sys.path.insert(0, './API')

import datetime

def updateDict( dict, week ):
  if week in dict:
    dict[week] = dict[week] + 1
  else:
    dict[week] = 1

def printResults(preprints, postprints):
  keyList = sorted(preprints.keys())
  for key in keyList: print(key, preprints[key],postprints[key])

# command line inputs
# logFile - full path to log file 
logFile = sys.argv[1]

# seperator for log file
sep = ';'
sep2 = ":"

# dictionaries
pre2017 = {}
pos2017 = {}
pre2018 = {}
pos2018 = {}
for i in range(52):
  w = i + 1
  pre2017[w] = 0
  pre2018[w] = 0
  pos2017[w] = 0
  pos2018[w] = 0

# open the log file
lFile = open(logFile, "r")
for line in lFile:

   parts = line.split(sep)
   identifier = parts[0]
   provider = parts[1]
   doi = parts[2]
   peer_review_doi = parts[3]
   date_published = parts[4]
   peer_review_date_published = parts[5]
   title = parts[6]
   authorList = parts[7]
   keywordList = parts[8]

   authors = authorList.split(sep2)
   keywords = keywordList.split(sep2)

   p1 = date_published.split("-")
   year1 = int(p1[0])
   month1 = int(p1[1])
   p1 = p1[2].split("T")
   day1 = int(p1[0])
   d1 = datetime.date(year1,month1,1)
   week = datetime.date(year1,month1,day1).isocalendar()[1]
   if (peer_review_doi != ""):
      p2 = peer_review_date_published.split("-")
      year2 = p2[0]
      month2 = p2[1]
      if ( (year2 == "") or (month2 == "") ):
         continue
      else:
         d2 = datetime.date(int(year2),int(month2),1)
         diff = (d2 - d1).days
         if ( diff < 0 ):
           if int(year1) == 2017:
             updateDict( pos2017, week )
           else:
             updateDict( pos2018, week )
         else:
           if int(year1) == 2017:
             updateDict( pre2017, week )
           else:
             updateDict( pre2018, week )
   else: # preprint
      if int(year1) == 2017:
         updateDict( pre2017, week )
      else:
         updateDict( pre2018, week )

# close the log file   
lFile.close()

printResults(pre2017, pos2017)
printResults(pre2018, pos2018)
