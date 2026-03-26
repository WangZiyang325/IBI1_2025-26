# This code creates a dictionary to store gene expression data, adds a new gene and its expression level, plots the gene expression levels using a bar chart, checks if a specific gene of interest is in the dataset and prints its expression level, and calculates the average expression level of all genes in the dataset.
import numpy as np
import matplotlib.pyplot as plt
# create a dictionary to store gene expression data
a = {'Gene':['TP53','EGFR','BRCA1','PTEN','ESR1'],
     'Expression':[12.4, 15.1, 8.2, 5.3, 10.7]}
# add a new gene and its expression level to the dictionary
a['Gene'].append('MYC')
a['Expression'].append(11.6) 
print(a)
# plot the gene expression levels using a bar chart
ax = plt.bar(a['Gene'], a['Expression'])
plt.xlabel('Gene')       
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels')
plt.show()

# creat a variable to store the gene of interest and check if it is in the dataset
gene_of_interest = "TP53"                   # my selected gene of interest
if gene_of_interest in a['Gene']:
    index = a['Gene'].index(gene_of_interest)
    print(f"\n{gene_of_interest} expression level: {a['Expression'][index]}")
else:
    print(f"\nError: {gene_of_interest} is not in the dataset!")


# calculate the average expression level of all genes in the dataset
average_expression = np.mean(a['Expression']) 
print('Average Expression Level:', average_expression)




