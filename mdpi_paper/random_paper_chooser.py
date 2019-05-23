import sys
import random

# command line inputs
inDir = sys.argv[1]
outFile = sys.argv[2]

# open the output file
oFile = open(outFile, "w")

# seperator for log file
sep = ';'

dirs = ["lissa", "marxiv", "mindrxiv", "eartharxiv", "paleorxiv", "engrxiv", "psyarxiv", "lawarxiv", "socarxiv" ]
for d in dirs:

  titles = []
  authors = []
  f = inDir + d + '/' + d + ".log"

  # open the log file
  lFile = open(f, "r")
  for line in lFile:

    parts = line.split(sep)
    peer_review_doi = parts[3]

    # doesn't have a peer reviewed doi
    if (peer_review_doi == "" ):
      titles.append(parts[6])
      authors.append(parts[7])

  # close the log file
  lFile.close()

  # choose 12 at random
  rtitles = random.sample(titles, 12)

  # write titles and authors to output file
  for title in rtitles:
    print(title, file=oFile)
    i = titles.index(title)
    print(authors[i], file=oFile)
    print(" ", file=oFile)

# close the output file
oFile.close()