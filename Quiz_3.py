# Usage : cat q3_first.tsv | python script.py q3_second.tsv > output.tsv
from sys import stdin,stdout,argv

# Context manager open and close itself with , q3_second.tsv is the argv[1]
with open(argv[1]) as second_file :
  # An empty dict is created
  sec_dict = {} 
  # Looping each line
  for line in second_file :
    # Striping the whitespaces with 1 spilting and adding the line to the list
    line_lt = line.strip().split("\t",maxsplit=1)
    # Zeroth index(ID) as key and later is value
    sec_dict[line_lt[0]] = line_lt[1]

# Looping each line into the q3_first.tsv using standard input
for row in stdin :
  # Striping the whitespaces with 1 spilting and adding the line to the list
  row_lt = row.strip().split("\t",maxsplit=1)
  # Checking if the Zeroth index(ID) is in dict
  if row_lt[0] in sec_dict :   
    # Writing in the output
    stdout.write(row.strip()+"\t"+sec_dict[row_lt[0]]+"\n")