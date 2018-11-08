import sys

log = sys.argv[1]

lf = open(log, "r")

journals = []

for line in lf:
  parts = line.split(";")
  identifier = parts[0].strip()
  provider = parts[1].strip()
  peer_review_doi = parts[2].strip()
  peer_review_date = parts[3].strip()
  peer_review_journal = parts[4].strip()
  print(identifier, provider)
  peer_review_title = parts[5].strip()
  peer_review_authors = parts[6].strip()
  peer_review_publisher = parts[7].strip()
  peer_review_url = parts[8].strip()
  if (peer_review_journal not in journals):
    journals.append(peer_review_journal)

lf.close()

print("Number of journals:", len(journals))

