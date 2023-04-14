import re
seq=''
header=''
input_file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') #read the file
out_file=open('TGA_gene.fa','w') # make a new file to store the output
for line in input_file:
  line=line.strip() #get rid of the blank space
  if line.startswith(">")and seq=='': #search the first line of the sequence
    x=line
    header=str(x[1:13]) #store the gene name
  elif line[0] !=">":
    seq=seq+line #store the sequence line
  elif line[0]==">"and seq!="": #meet a new sequence
    if seq.endswith("TGA"): #find the stop codon
      out_file.write(header+'\n'+seq+'\n') 
      seq=''
      header=str(x[1:13])
if seq.endswith('TGA'):
  out_file.write(header+'\n'+seq+'\n')
input_file.close()
out_file.close()


