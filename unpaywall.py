import sys
import json
import requests
sys.path.insert(0, './API')

import datetime

headers = {'Content-Type': 'application/json'}

# command line inputs
# logFile - full path to log file 
logFile = sys.argv[1]

# seperator for log file
sep = ';'

# counters
total = 0
isOA = 0
isNotOA = 0
errors = 0

# open the log file
lFile = open(logFile, "r")
for line in lFile:

   parts = line.split(sep)
   peer_review_doi = parts[3]

   if (peer_review_doi != "" ):
     total += 1
     p = peer_review_doi.split("/")
     l = len(p)
     if (l == 5):
       url = "https://api.unpaywall.org/v2/" + p[-2].strip() + "/" + p[-1].strip() + "?email=tnarock@ndm.edu"
     if (l == 6):
       url = "https://api.unpaywall.org/v2/" + p[-3].strip() + "/" + p[-2].strip() + "/" + p[-1].strip() + "?email=tnarock@ndm.edu"
     response = requests.get(url, headers=headers)
     if ( response.status_code == 200 ):
        json_object = json.loads(response.content.decode('utf-8'))
        r = json_object['is_oa']
        if ( r == True ):
          isOA += 1
        if ( r == False ):
          isNotOA += 1
     else:
        errors += 1

# close the log file   
lFile.close()

print("Total number of papers", total)
print("OA", isOA)
print("Not OA", isNotOA)
print("Unclassifiable", errors)
