def getMatchingAuthors(lastNames, lastName):

    index = 0
    possibleMatches = []
    for lname in lastNames:
      if (lname == lastName):
         possibleMatches.append(index)
      index += 1

    return possibleMatches

import sys

# command line inputs
inDir = sys.argv[1]
outFile = sys.argv[2]

# seperator for log file
sep = ';'
sep2 = ":"

# counters
totalAuthors = 0
conflicts = []

# lists to hold author names
firstNames = []
lastNames = []

dirs = ["lissa", "marxiv", "mindrxiv", "eartharxiv", "paleorxiv", "engrxiv", "psyarxiv", "lawarxiv", "socarxiv" ]
for d in dirs:

  authors = []
  f = inDir + d + '/' + d + ".log"

  # open the log file
  lFile = open(f, "r")
  for line in lFile:

    parts = line.split(sep)
    authors = parts[7].split(sep2)
    for author in authors:
      totalAuthors += 1
      parts = author.strip().split(" ")
      if ( len(parts) > 1 ): # do we have a valid name?

         if ( len(parts) == 3 ): # we have a middle initial
            firstName = parts[0].strip()
            lastName = parts[2].strip()
         else:
            firstName = parts[0].strip()
            lastName = parts[1].strip()

         possibleMatches = getMatchingAuthors(lastNames, lastName)
         for pm in possibleMatches:
      
            fname = firstNames[pm]

            if ( fname != firstName ):

               # does first initial match?
               fi = firstName[0]
               if ( fi.lower() == fname[0].lower() ):
                  conflict = author + ", " + fname + " " + lastNames[pm]
                  if (conflict not in conflicts):
                    conflicts.append(conflict)
      
         firstNames.append( firstName )
         lastNames.append( lastName )

  # close the log file
  lFile.close()

ofile = open(outFile, "w")
print("Total Authors", totalAuthors, file=ofile)
for conflict in conflicts:
   print(conflict, file=ofile)