import sys

def outputDict(dict, year, month, outDir):

   file = outDir + 'eartharxiv_keyword_counts_' + year + '_' + month + '.log'
   fh = open(file, "w")

   sorted_d = sorted( (value, key) for (key, value) in dict.items() )

   for key, value in sorted_d:
     fh.write(str(key).strip() + "," + str(value).strip() + "\n")
   
   fh.close()
   
def updateDictionary(dict, keyword):
   if (keyword in dict):
     value = dict[keyword]
     dict[keyword] = value + 1
   else:
     dict[keyword] = 1

logFile = sys.argv[1]
outDir = sys.argv[2]

# dictionaries to hold the results
key201710 = {}
key201711 = {}
key201712 = {}
key201801 = {}
key201802 = {}
key201803 = {}
key201804 = {}
key201805 = {}
key201806 = {}
key201807 = {}
key201808 = {}
key201809 = {}
key201810 = {} 

# open the keyword log file
klf = open(logFile, "r")

# loop over all the lines in the log file
for line in klf:

   parts = line.split(";") # keyword;dateTime
   keyword = parts[0].strip()
   dateTime = parts[1].strip()
   parts = dateTime.split("T")
   date = parts[0].strip()
   parts = date.split("-")
   year = int(parts[0].strip())
   month = int(parts[1].strip())
   day = int(parts[2].strip())

   # put the keyword in the correct dictionary
   ## there's probably a better way to do this!
   if (year == 2017):
      if month == 10: updateDictionary(key201710, keyword) 
      if month == 11: updateDictionary(key201711, keyword) 
      if month == 12: updateDictionary(key201712, keyword) 
   if (year == 2018):
      if month == 1: updateDictionary(key201801, keyword) 
      if month == 2: updateDictionary(key201802, keyword) 
      if month == 3: updateDictionary(key201803, keyword) 
      if month == 4: updateDictionary(key201804, keyword) 
      if month == 5: updateDictionary(key201805, keyword) 
      if month == 6: updateDictionary(key201806, keyword)
      if month == 7: updateDictionary(key201807, keyword) 
      if month == 8: updateDictionary(key201808, keyword) 
      if month == 9: updateDictionary(key201809, keyword) 
      if month == 10: updateDictionary(key201810, keyword) 
      if month == 11: updateDictionary(key201811, keyword) 
      if month == 12: updateDictionary(key201812, keyword) 

# close the keyword log file
klf.close()

# output the results
outputDict(key201710, '2017', '10', outDir)
outputDict(key201711, '2017', '11', outDir)
outputDict(key201712, '2017', '12', outDir)
outputDict(key201801, '2018', '01', outDir)
outputDict(key201802, '2018', '02', outDir)
outputDict(key201803, '2018', '03', outDir)
outputDict(key201804, '2018', '04', outDir)
outputDict(key201805, '2018', '05', outDir)
outputDict(key201806, '2018', '06', outDir)
outputDict(key201807, '2018', '07', outDir)
outputDict(key201808, '2018', '08', outDir)
outputDict(key201809, '2018', '09', outDir)
outputDict(key201810, '2018', '10', outDir)
#outputDict(key201811, '2018', '11', outDir)
#outputDict(key201812, '2018', '12', outDir)



