import random as rd
import Bio
from collections import Counter
from Bio.Seq import Seq

NUC = ['A','T','G','C']

DNA = rd.choices(NUC, k=90)
columns = ''.join(['|' for _ in range(len(DNA))])
DNA = Seq(''.join(DNA))
RNA = DNA.transcribe()
Protein = RNA.translate()

RNA = str(RNA)
DNA = str(DNA)


print(f"+ DNA Nuc Counter: {Counter(DNA)}\n+ RNA Nuc Counter: {Counter(RNA)}\n\n{DNA}\n{columns}\n{RNA}\n\nProtein:\n{Protein}")
