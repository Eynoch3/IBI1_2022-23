
def protein_coding(sequence):
 import re
 #input a sequence with ATG codon and TGA codon
 seq=sequence.upper() #exchange all the cases into upper case
 count=0
 start_codon=seq.find('ATG') #find the position of the start codon
 stop_codon=seq.find('TGA',start_codon+3) #find the position of the stop codon
 aim_seq_length=stop_codon-start_codon+3 #the length of the aim sequence
 total_length=len(seq)
 percentage=aim_seq_length/total_length
 if percentage>0.5:
   print ('the percentage of this sequence is',str(percentage),',so the sequence is labelled as protein-coding')
 elif percentage<0.1:
   print ('the percentage of this sequence is',str(percentage),',so the sequence is lablled as non-coding')
 else:
   print ('the percentage of this sequence is',str(percentage),',so the sequence is lablled as unclear')    
#example
sequence='gggATGATGGGTTTTGGCCCTGTCGGTGTAGCTTGATGCTAG' # can change the sequnece to get the result
protein_coding(sequence)



