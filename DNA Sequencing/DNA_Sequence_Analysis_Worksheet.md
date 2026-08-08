# DNA Sequence Analysis — Worksheet

## Goal
You'll build a small toolkit of Python functions that work with DNA sequences —
the same kind of operations real bioinformatics tools perform every day.

You are given:
- `dna_analysis.py` — starter code with function **stubs** for you to fill in
- `test_dna_analysis.py` — a test suite that checks your work

### How to work through this
1. Open `dna_analysis.py`.
2. Implement each function one at a time, following the docstring instructions.
3. After each function, run the tests to check your progress:
   ```
   python -m unittest test_dna_analysis.py -v
   ```
4. Don't move to the next function until the current one passes its tests.
5. If you get stuck, use `print()` statements inside your function to inspect
   what's happening with small example strings.

---

## Background you need

**DNA** is made of 4 bases: `A`, `T`, `C`, `G`.
**RNA** uses `U` instead of `T`.

Base pairing rules (complementary bases):
- A pairs with T (or U in RNA)
- C pairs with G

**Transcription**: DNA → RNA. Every `T` becomes `U`, everything else stays the same.

**The reverse complement** is used constantly in biology because DNA is
double-stranded and the strands run in opposite directions. To get it:
1. Reverse the sequence
2. Swap each base for its complement (A↔T, C↔G)

**Translation**: RNA → Protein. RNA is read in groups of 3 bases called
**codons**. Each codon maps to one amino acid (or a "stop" signal) using
the genetic code. Translation starts at the codon `AUG` (which also codes
for the amino acid Methionine, `M`) and stops at one of the stop codons:
`UAA`, `UAG`, `UGA`.

**GC content** is the percentage of bases in a sequence that are G or C.
It matters biologically because GC-rich regions of DNA are more stable
(3 hydrogen bonds vs. 2 for A-T pairs) and it's used to compare species,
identify genes, and design lab experiments (like PCR primers).

**Open Reading Frames (ORFs)** are stretches of sequence that start with
`ATG` and run in multiples of 3 bases until a stop codon — these are the
regions of DNA that could potentially be translated into a protein.

---

## Functions to implement (in order of difficulty)

### 1. `count_nucleotides(seq)`
Count how many times each base (A, T, C, G) appears in a DNA sequence.
Returns a dictionary, e.g. `{'A': 2, 'T': 1, 'C': 0, 'G': 3}`.

### 2. `gc_content(seq)`
Calculate the GC content of a DNA sequence as a percentage (0–100),
rounded to 2 decimal places.

### 3. `transcribe(dna_seq)`
Convert a DNA sequence into its RNA equivalent (replace T with U).

### 4. `reverse_complement(dna_seq)`
Return the reverse complement of a DNA sequence.

### 5. `translate(rna_seq)`
Translate an RNA sequence into a protein sequence using the codon table
provided in the starter code. Stop translating (and don't include it in
the output) when you hit a stop codon.

### 6. `find_motif(seq, motif)`
Find **all** starting positions (0-indexed) where a given motif
(short sequence) occurs in a larger sequence. Return a list of positions.
Hint: motifs can overlap — think about how you scan through the sequence.

### 7. `find_orfs(dna_seq)`
Find all Open Reading Frames in a DNA sequence: every substring that
starts with `ATG` and ends at the next in-frame stop codon
(`TAA`, `TAG`, `TGA`), reading in steps of 3. Return a list of the
ORF DNA substrings (including the start and stop codon).

---

## Stretch goals (optional, once everything passes)
- Modify `find_orfs` to also search the reverse complement strand
  (real genes can be on either strand of the DNA double helix).
- Write a function `hamming_distance(seq1, seq2)` that counts how many
  positions differ between two equal-length sequences — this is a basic
  way to measure mutations between two versions of a gene.
- Try your functions on a real gene! Look up a short gene sequence on
  [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/) and run it through
  your toolkit.

## Reflection questions (answer in a few sentences each)
1. Why do you think biologists care about GC content when designing lab experiments?
2. Why does translation always start at `ATG` specifically?
3. What real-world problem could `find_motif` help solve? (Hint: think about looking for a specific gene, mutation, or CRISPR target site.)
