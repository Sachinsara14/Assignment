# Usage : python script.py < q2_data.tsv
import matplotlib.pyplot as plt 
import pandas as pd 
from sys import stdin

# Converting the tsv into dataframe structure with headers ["x-axis","y-axis","genes"]
all_data = pd.read_csv(stdin,sep="\t",header=None,names=["x-axis","y-axis","genes"])

# Using groupby so that each gene has its own line in graph 
for gene,data in all_data.groupby("genes") :
  plt.plot(data["x-axis"],data["y-axis"],label=gene)

# Lable box is shown
plt.legend()
# Saving in the output file 
plt.savefig("output.png")