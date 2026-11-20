from Bio.Seq import Seq

genome = Seq("ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAG")

print(f"طول الجينوم: {len(genome)}")
print(f"GC%: {round((genome.count('G')+genome.count('C'))/len(genome)*100, 2)}%")
print("الجينوم سليم - BioIlham Project")
