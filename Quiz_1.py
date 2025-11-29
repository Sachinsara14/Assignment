# Usage : cat q1_data.tsv | python script.py to_select.tsv 2 > output.tsv
from sys import stdin,stdout,argv

# Getting the index of column
col_ind = int(argv[2]) - 1
# Context manager open and close itself with , query.tsv is the argv[1]
with open(argv[1]) as query :
  # Set comprehension for storing each queries
  query_st = {line.strip() for line in query}

# Looping each line into the big_file.tsv using standard input 
for row in stdin:
  # Striping the whitespaces and spliting with tab
  big_file_lt = row.strip().split("\t")
  # Checking if the 2nd column (1st index) matches with the elements in sets from query
  if big_file_lt[col_ind] in query_st :   
    # If matches the line is written in output.tsv file 
    stdout.write(row)