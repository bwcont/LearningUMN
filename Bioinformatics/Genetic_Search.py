#############################
#####Genetic Searching#######
#############################

#From Bioinformatics Programming using Python O'Reilly 2009

#import a random number generator
from random import randint

"""create a random base generator where we return a single letter.
the parameter is whether we want to return an RNA nucleotide letter
If nothing is specified, it will default to a DNA nucleotide.
The bracketed code tells the code to only give us one random letter
between 0 and 3."""

def random_base(RNAflag = False):
    return ('UCAG' if RNAflag else 'TCAG') [randint(0,3)]
  
"""Next we want to make a codon using the random letters we generated above"""
def random_codon(RNAflag = False):
    return random_base(RNAflag) + random_base(RNAflag) +random_base(RNAflag)

#test:
print ("random codon test:")
print(random_codon())
