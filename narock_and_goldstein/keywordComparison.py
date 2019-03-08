import sys
import itertools

dir = sys.argv[1]

keywords = {}
repos = ['eartharxiv', 'engrxiv', 'lawarxiv', 'lissa', 'marxiv', 'paleorxiv', 'psyarxiv', 'socarxiv']

for repo in repos:

   file = dir + repo + '/logs/' + repo + '_keywords_count.log'
   f = open(file, 'r')
   for line in f:
      parts = line.split(';')
      keyword = parts[0].strip()
      count = parts[1].strip()
      if (keyword in keywords):
        lst = keywords[keyword]
        lst.append( repo )
      else:
        lst = [repo]
        keywords[keyword] = lst

   f.close() 

# eartharxiv, engrxiv, lawarxiv, lissa, marxiv, mindrxiv, paleorxiv, psyarxiv, socarxiv
pairs = {}
for key, value in keywords.items():
   if ( len(value) > 1 ):
      for pair in itertools.combinations(value,2):
         r1, r2 = pair
         option1 = r1.strip() + "-" + r2.strip()
         option2 = r2.strip() + "-" + r1.strip()
         if (option1 in pairs):
            count = pairs[option1]
            pairs[option1] = count + 1
         elif (option2 in pairs):
            count = pairs[option2]
            pairs[option2] = count + 1
         else:
            pairs[option1] = 1 

for key, value in pairs.items():
   print(key, value)
