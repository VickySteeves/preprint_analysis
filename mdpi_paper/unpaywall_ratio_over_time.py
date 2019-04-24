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

# seperator for log file
sep = ';'

years = {}

# open the log file
lFile = open(logFile, "r")
for line in lFile:

   parts = line.split(sep)
   peer_review_doi = parts[3]
   preprint_date = parts[4]

   parts = preprint_date.split("-")
   year = parts[0]
   if (year in years):
      dois = years[year]
      dois.append( preprint_date + ";" + peer_review_doi )
      years[year] = dois
   else:
      years[year] = [ preprint_date + ";" + peer_review_doi ]

lFile.close()

for key, value in years.items():

   # counters
   total = 0
   errors = 0
   preprints = 0
   postprints = 0

   print(key)

   for d in value:
     p = d.split(";")
     preprint_date = p[0].strip()
     doi = p[1].strip()
     if (doi != "" ):
       total += 1
       p = doi.split("/")
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
       else:
        errors += 1

     else:
        preprints += 1
        total += 1

   print(" Total number of papers", total)
   print(" Confirmed postprints", postprints)
   print(" Confirmed preprints", preprints)
   print(" Couldn't be classified", errors)
