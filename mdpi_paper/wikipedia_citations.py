import csv

def read_wikipedia(file):

  dois = []
  pageTitles = []

  # read the wikipedia data and extract all the DOIs
  # we can't match arxiv, isbn, or pubmed identifiers
  with open(file, 'r') as f:
    next(f) # skip header
    reader = csv.reader(f, delimiter='\t')
    for page_id, page_title, revision_id, timestamp, type, id in reader:
       if ( type.strip() == 'doi' ):
          dois.append(id.lower())
          pageTitles.append( page_title )
  f.close()

  return dois, pageTitles

def compare_with_wikipedia(logFile, dois, pageTitles):

  # open the preprint log file
  preprint_count = 0
  peer_review_count = 0
  f = open(logFile, 'r')
  for line in f:
     parts = line.split(';')
     identifier = parts[0]
     doi = parts[2]
     doi = doi[19:].lower()
     peer_review_doi = parts[3]
     if ( peer_review_doi != '' ):
        peer_review_doi = peer_review_doi[19:].lower()
        if ( peer_review_doi in dois ):
           peer_review_count += 1

     if ( doi in dois ):
        preprint_count += 1 
        indx = dois.index(doi)
        print(doi, pageTitles[indx])

  f.close()

  print("  Found", preprint_count, "preprint DOIs")
  print("  Found", peer_review_count, "peer reviewed DOIs")
