import sys
sys.path.insert(0, './API')

import datetime

# command line inputs
# logFile - full path to log file 
logFile = sys.argv[1]
delayFile = sys.argv[2]
keywordTimestampFile = sys.argv[3]
keywordCountFile = sys.argv[4]

# seperator for log file
sep = ';'
sep2 = ":"

# counters
preprints = 0
postprints = 0
pre_postprints = 0
peerReviewed = 0
unableToGetPeerReviewDate = 0
totalAuthors = 0

# lists
delay = []
distinctAuthors = []

# dictionaries
keywordDict = {}

# open the keyword timestamp file for writing
keyTime = open(keywordTimestampFile, "w")

# open the log file
lFile = open(logFile, "r")
for line in lFile:

   pre_postprints += 1

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

   for author in authors:
      author = author.strip()
      totalAuthors += 1
      if (author not in distinctAuthors):
        distinctAuthors.append(author)

   for keyword in keywords:
      keyword = keyword.strip()
      keyTime.write(keyword + sep + date_published + "\n")
      if (keyword in keywordDict):
         count = keywordDict[keyword]
         keywordDict[keyword] = count+1
      else:
         keywordDict[keyword] = 1

   if (peer_review_doi != "" ):
      peerReviewed += 1
      p1 = date_published.split("-")
      p2 = peer_review_date_published.split("-")
      year1 = p1[0]
      month1 = p1[1]
      year2 = p2[0]
      month2 = p2[1]
      d1 = datetime.date(int(year1),int(month1),1)
      if ( (year2 == "") or (month2 == "") ):
         unableToGetPeerReviewDate += 1
      else:
         d2 = datetime.date(int(year2),int(month2),1)
         diff = (d2 - d1).days
         if ( diff < 0 ):
           postprints += 1
         else:
           delay.append(diff)
           preprints += 1

# close keyword timestamp file
keyTime.close()

# what is the average delay time?
sum = 0
oFile = open(delayFile, "w")
for d in delay:
  sum += d
  oFile.write( str(d) + "\n" )
print("Delay between preprint and peer-review:", float(sum/len(delay)))
oFile.close()

print( str(pre_postprints) + " total papers")
print( str(peerReviewed) + " papers also have a peer-reviewed DOI")
print( "  " + str(postprints) + " of these are confirmed postprints")
print( "  " + str(unableToGetPeerReviewDate) + " of these can't get peer review date")
print( "  " + str(preprints) + " of these are confirmed preprints")
print(" ")
print( str(len(distinctAuthors)) + " distinct authors out of " + str(totalAuthors) + " total authors")

kcf = open(keywordCountFile, "w")
for key, value in keywordDict.items():
  kcf.write(key.strip() + sep + str(value) + "\n")
kcf.close()

# close the log file   
lFile.close()
