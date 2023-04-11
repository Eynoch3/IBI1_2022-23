import re
seq=''
header=''
input_file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
out_file=open('TGA_gene.fa','w')
for line in input_file:
  line=line.strip()
  if line.startswith(">")and seq=='':
    x=line
    header=str(x[1:13])
  elif line[0] !=">":
    seq=seq+line
  elif line[0]==">"and seq!="":
    if seq.endswith("TGA"):
      out_file.write(header+'                              '+seq+'                     ')
      seq=''
      header=str(x[1:13])
if seq.endswith('TGA'):
  out_file.write(header+'                                 '+seq+'                       ')
input_file.close()
out_file.close()
with open('TGA_gene.fa','r')as look:
  print (look.read())
look.close()

