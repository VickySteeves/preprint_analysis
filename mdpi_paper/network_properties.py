import networkx as nx
import itertools
import sys

def main():

    # command line inputs
    # logFile - full path to log file 
    logFile = sys.argv[1]
    outFile = sys.argv[2]

    # seperator for log file
    sep = ';'
    sep2 = ":"

    # lists we'll need
    uniqueAuthors = []
    edges = []

    # open the log file
    lFile = open(logFile, "r")
    for line in lFile:

        parts = line.split(sep)

        authorList = parts[7] # this is a string
        authors = authorList.split(sep2) # now a list

        # find all the pairwise author combinations so we can create edges between them
        for pair in itertools.combinations(authors,2):
            author1, author2 = pair            
            author1 = author1.strip() # clean up the names, remove leading and trailing spaces
            author2 = author2.strip()

            if ( author1 not in uniqueAuthors ):
                uniqueAuthors.append(author1)

            if ( author2 not in uniqueAuthors ):
                uniqueAuthors.append(author2)

            # create edges if they don't alredy exist
            e1 = (author1, author2)
            e2 = (author2, author1)
            if ( (e1 not in edges) and (e2 not in edges) ):
                edges.append(e1)
                    
    lFile.close()

    # create a networkx graph object
    graph = nx.Graph()
    graph.add_nodes_from( uniqueAuthors )
    graph.add_edges_from( edges )
    
    # open the output file
    oFile = open(outFile, "w")

    # compute connected components
    ccs = list(nx.connected_component_subgraphs(graph))    
    for cc in ccs:
        print( nx.number_of_nodes(cc), file=oFile )
        
    # close the output file        
    oFile.close()

main()
