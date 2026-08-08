"""
DNA Sequence Analysis Toolkit
------------------------------
Fill in each function below according to its docstring.
Run test_dna_analysis.py after each one to check your work.

    python -m unittest test_dna_analysis.py -v
"""

# The standard RNA codon table: maps each 3-letter RNA codon to a 1-letter
# amino acid code. '*' means STOP.
CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

DNA_STOP_CODONS = {'TAA', 'TAG', 'TGA'}
COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def count_nucleotides(seq):
    nucleotides = {}
    for x in seq:
        if x not in nucleotides.keys():
            nucleotides[x] = 1
        else:
            nucleotides[x] += 1
    return nucleotides


def gc_content(seq):
    a = count_nucleotides(seq)
    percent = (a["G"] + a["C"]) / (a["A"] + a["G"] + a["C"] + a["T"])
    return percent


def transcribe(dna_seq):
    rna = ""
    for x in dna_seq:
        if x == "T":
            rna += "U"
        else:
            rna += x

    return rna

def reverse_complement(dna_seq):

    newStrand = ""
    for x in dna_seq:
        newStrand += COMPLEMENT[x]

    return newStrand

def translate(rna_seq):

    newStrand = ""
    for x in range(0, round(len(rna_seq)), 3):
        if CODON_TABLE[rna_seq[x:x+3]] == "*":
            break
        newStrand += CODON_TABLE[rna_seq[x:x+3]]
    return newStrand


def find_motif(seq, motif):
    positions = []
    for x in range(0, len(seq) - len(motif)):
        viewing = seq[x:x+len(motif)]
        if viewing == motif:
            positions.append(x)

    return positions


def find_orfs(dna_seq):
    currentOrfs = {}
    orfs = []
    for idx, x in enumerate(range(0, round(len(dna_seq)), 3)):
        viewing = dna_seq[x:x+3]
        if viewing == "ATG":
            currentOrfs[idx] = viewing
            marker = idx
        elif viewing in DNA_STOP_CODONS:
            currentOrfs[marker] += viewing
            orfs.append(currentOrfs[marker])
        else:
            currentOrfs[marker] += viewing

    return orfs


       
    """
    Find all Open Reading Frames (ORFs) in a DNA sequence.

    An ORF is a substring that:
      - starts with the codon "ATG"
      - is read in steps of 3 from there
      - ends at the next in-frame stop codon (TAA, TAG, or TGA)
    The returned substring should include both the start codon and the
    stop codon.

    Search only the given strand (left to right) -- you do not need to
    check the reverse complement for this exercise (that's a stretch goal).
    If a start codon doesn't reach an in-frame stop codon before the
    sequence ends, it does not count as an ORF.

    Args:
        dna_seq (str): a DNA sequence

    Returns:
        list[str]: all ORFs found, in the order their start codons appear

    Example:
        >>> find_orfs("XXATGAAATAGXXXATGCCCTGAXX")
        ['ATGAAATAG', 'ATGCCCTGA']
    """
    # TODO: implement this function
    raise NotImplementedError


if __name__ == "__main__":
    # Quick manual sandbox -- feel free to experiment here as you work!
    sample = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    print("Sample sequence:", sample)
    # Uncomment these as you implement each function:

    print("Nucleotide counts:", count_nucleotides(sample))
    print("GC content:", gc_content(sample))
    print("Transcribed:", transcribe(sample))
    print("Reverse complement:", reverse_complement(sample))
    print("Translated:", translate(transcribe(sample)))
    print("Motif 'GGC' found at:", find_motif(sample, "GGC"))
    print("ORFs found:", find_orfs(sample))
