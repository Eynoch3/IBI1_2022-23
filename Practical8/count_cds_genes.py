import re
stop_codon=input('Enter the stop codon(TAA,TAG or TGA):') 
#input one of the three stop codons'TAA','TAG'or'TGA'
out_file=f'{stop_codon}_stop_genes.fa'
#output fasta file

#open input and output file
input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output_file=open(out_file,'w')
gene_name='' #store the gene name
seq='' #store the sequence
count=1
for line in  input_file:
 line=line.strip()
 if line.startswith('>'):
   if seq.endswith(stop_codon): #check the presequence is ended with the stop codon
      output_file.write(gene_name+'     '+str(count)+'coding sequence'+'\n'+seq+'\n')
      count=count+1 #increment count of coding sequence
   gene_name=str(line[1:13]) #store the gene name
   seq='' #reset the sequence variable
 else:
   seq=seq+line #concatenate sequence
if seq.endswith(stop_codon): #check the last sequence
 output_file.write(gene_name+'     '+str(count)+'coding sequence'+'\n'+seq+'\n')
 count=count+1
print (f'Sequences of genes ending with {stop_codon} written to {out_file}.')

input_file.close()
output_file.close() 
