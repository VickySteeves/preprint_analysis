import sys
import wikipedia_citations

file = sys.argv[1] 
dir = sys.argv[2] 
#arxivs = ['eartharxiv', 'engrxiv', 'lawarxiv', 'lissa', 'marxiv', 'mindrxiv', 'paleorxiv', 'psyarxiv', 'socarxiv']
arxivs = ['socarxiv']

dois, pageTitles = wikipedia_citations.read_wikipedia(file)

for i in arxivs:
   print( "Working on", i )
   f = dir + i + '/' + i + '.log'
   wikipedia_citations.compare_with_wikipedia( f, dois, pageTitles )
   print()
