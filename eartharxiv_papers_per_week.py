import sys
import json
import requests
from datetime import date
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
email = sys.argv[2]

# seperator for log file
sep = ';'
sep2 = ":"

# dictionaries
pre2017 = {}
pos2017 = {}
pre2018 = {}
pos2018 = {}
pre2019 = {}
pos2019 = {}
for i in range(52):
  w = i + 1
  pre2017[w] = 0
  pre2018[w] = 0
  pre2019[w] = 0
  pos2017[w] = 0
  pos2018[w] = 0
  pos2019[w] = 0

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

      headers = {'Content-Type': 'application/json'}
      p = peer_review_doi.split("/")
      l = len(p)
      if (l == 5):
        url = "https://api.unpaywall.org/v2/" + p[-2].strip() + "/" + p[-1].strip() + "?email=" + email.strip()
      if (l == 6):
        url = "https://api.unpaywall.org/v2/" + p[-3].strip() + "/" + p[-2].strip() + "/" + p[-1].strip() + "?email=" + email.strip()
      response = requests.get(url, headers=headers)
      if ( response.status_code == 200 ):
        json_object = json.loads(response.content.decode('utf-8'))
        published_date = json_object['published_date']

        # publication delay
        preprint = date_published.split("T")
        preprint = preprint[0].split("-")
        if ( published_date is None ):
           continue 
        else:
           j = published_date.split("-")
           d0 = date( year1, month1, day1 )
           d1 = date(int(j[0]), int(j[1]), int(j[2]))        
           delta = d1 - d0
           if (delta.days <= 0):
              if ( year1 == 2017 ):
                updateDict( pos2017, week ) 
              elif ( year1 == 2018 ):
                updateDict( pos2018, week )
              else:
                updateDict( pos2019, week )
           else:
              if ( year1 == 2017 ):
                updateDict( pre2017, week )
              elif ( year1 == 2018 ):
                updateDict( pre2018, week )
              else:
                updateDict( pre2019, week )

   else:
       if ( year1 == 2017 ):
         updateDict( pre2017, week )
       elif ( year1 == 2018 ):
         updateDict( pre2018, week )
       else:
         updateDict( pre2019, week )

# close the log file   
lFile.close()

printResults(pre2017, pos2017)
printResults(pre2018, pos2018)
#printResults(pre2019, pos2019)
