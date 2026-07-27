dna_sequence = "ATGCGAT"
pattern = "AGC"

def count_nucleotides(sequence):

    nucleotides = {}
    for x in sequence:
        if x not in nucleotides.keys():
            nucleotides[x] = 1
        else:
            nucleotides[x] += 1

    return nucleotides
    
def complementary_strand(sequence):
    newStrand = ""
    opposites = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for x in sequence:
        newStrand += opposites[x]

    return newStrand

def find_pattern(sequence, pattern):
    positions = []
    for x in range(0, len(sequence) - len(pattern)):
        currentslice = sequence[x:x+len(pattern)]
        if currentslice == pattern:
            positions.append(x)

    return positions

def transcribe_DNA_to_RNA(sequence):
    rna = ""
    for x in sequence:
        if x == "T":
            rna += "U"
        else:
            rna += x

    return rna

def gc_content(sequence):
    a = count_nucleotides(sequence)
    percent = (a["G"] + a["C"]) / (a["A"] + a["G"] + a["C"] + a["T"])

    return percent

a = gc_content(dna_sequence)
print(a)