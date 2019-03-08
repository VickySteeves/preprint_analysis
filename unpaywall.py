import sys
import json
import requests
from datetime import date
sys.path.insert(0, './API')

import datetime

headers = {'Content-Type': 'application/json'}

# command line inputs
# logFile - full path to log file 
logFile = sys.argv[1]
email = sys.argv[2]
delayLog = sys.argv[3]

# open for writing
dFile = open(delayLog, "w")

# seperator for log file
sep = ';'

# counters
total = 0
isOA = 0
isNotOA = 0
errors = 0
ujournals = 0
journals = []
preprints = 0
postprints = 0

# open the log file
lFile = open(logFile, "r")
for line in lFile:

   parts = line.split(sep)
   preprint_date = parts[4]
   peer_review_doi = parts[3]

   if (peer_review_doi != "" ):
     total += 1
     p = peer_review_doi.split("/")
     l = len(p)
     if (l == 5):
       url = "https://api.unpaywall.org/v2/" + p[-2].strip() + "/" + p[-1].strip() + "?email=" + email.strip()
     if (l == 6):
       url = "https://api.unpaywall.org/v2/" + p[-3].strip() + "/" + p[-2].strip() + "/" + p[-1].strip() + "?email=" + email.strip()
     response = requests.get(url, headers=headers)
     if ( response.status_code == 200 ):
        json_object = json.loads(response.content.decode('utf-8'))
        r = json_object['is_oa']
        journal = json_object['journal_name']
        published_date = json_object['published_date']
        if (journal not in journals):
           ujournals += 1
           journals.append(journal)
        if ( r == True ):
          isOA += 1
        if ( r == False ):
          isNotOA += 1

        # publication delay
        preprint = preprint_date.split("T")
        preprint = preprint[0].split("-")
        if ( published_date is None ):
           errors += 1
        else:
           j = published_date.split("-")
           d0 = date(int(preprint[0]), int(preprint[1]), int(preprint[2]))
           d1 = date(int(j[0]), int(j[1]), int(j[2]))        
           delta = d1 - d0
           if (delta.days <= 0):
              postprints += 1
           else:
              preprints += 1
           print(delta.days, file=dFile)
     else:
        errors += 1

# close the log files  
lFile.close()
dFile.close()

print("Total number of papers", total)
print("OA", isOA)
print("Not OA", isNotOA)
print("Unclassifiable", errors)
print("Unique journals", ujournals)
print("Confirmed postprints", postprints)
print("Confirmed preprints", preprints)
