# Usage = python script.py 4 < q4_data.tsv > output.tsv
# Usage = python script.py 4 < first_hundred_numbers.tsv > output2.tsv
from sys import stdin,stdout,argv
import pandas as pd

# Storing the input in a dataframe
num_df = pd.read_csv(stdin, header=None, names=["numbers"])

# Qualitile divisor is taken from the user
div = int(argv[1])

# Using qcut , the unsorted input is sorted and qualitile is found and labled 
num_df["q_range1"] = pd.qcut( num_df["numbers"] , q = div, labels=[f"q{i+1}" for i in range(div)])
# Coping the other key
num_df["q_range2"] = num_df["q_range1"] 

# The range of qualitile is found
num_df["quantile"] = pd.qcut( num_df["numbers"] , q = div)

# Using to_csv the tsv 
num_df.to_csv(stdout,sep = "\t",index=False,header=False)