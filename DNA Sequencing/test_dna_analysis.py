"""
Test suite for dna_analysis.py

Run with:
    python -m unittest test_dna_analysis.py -v

Each test class corresponds to one function in dna_analysis.py.
Tests within a class run from simplest to trickiest case.
"""

import unittest
from dna_analysis import (
    count_nucleotides,
    gc_content,
    transcribe,
    reverse_complement,
    translate,
    find_motif,
    find_orfs,
)


class TestCountNucleotides(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            count_nucleotides("AATTCG"),
            {'A': 2, 'T': 2, 'C': 1, 'G': 1}
        )

    def test_all_same_base(self):
        self.assertEqual(
            count_nucleotides("AAAA"),
            {'A': 4, 'T': 0, 'C': 0, 'G': 0}
        )

    def test_empty_sequence(self):
        self.assertEqual(
            count_nucleotides(""),
            {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        )


class TestGCContent(unittest.TestCase):
    def test_fifty_percent(self):
        self.assertEqual(gc_content("ATCG"), 50.0)

    def test_all_gc(self):
        self.assertEqual(gc_content("GGCC"), 100.0)

    def test_no_gc(self):
        self.assertEqual(gc_content("ATAT"), 0.0)

    def test_rounding(self):
        # 1 out of 3 = 33.333...%
        self.assertEqual(gc_content("ATG"), 33.33)

    def test_empty_sequence(self):
        self.assertEqual(gc_content(""), 0.0)


class TestTranscribe(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(transcribe("ATCG"), "AUCG")

    def test_all_t(self):
        self.assertEqual(transcribe("TTTT"), "UUUU")

    def test_no_t(self):
        self.assertEqual(transcribe("ACGG"), "ACGG")


class TestReverseComplement(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(reverse_complement("ATCG"), "CGAT")

    def test_palindromic(self):
        # This sequence is its own reverse complement
        self.assertEqual(reverse_complement("GAATTC"), "GAATTC")

    def test_single_base(self):
        self.assertEqual(reverse_complement("A"), "T")


class TestTranslate(unittest.TestCase):
    def test_simple_with_stop(self):
        self.assertEqual(translate("AUGGCCUAA"), "MA")

    def test_no_stop_codon(self):
        # Sequence ends before hitting a stop codon
        self.assertEqual(translate("AUGGCC"), "MA")

    def test_immediate_stop(self):
        self.assertEqual(translate("UAAAUGGCC"), "")

    def test_longer_sequence(self):
        # AUG GCC AUU GUA AUG GGC CGC UGA -> M A I V M G R (stop)
        self.assertEqual(
            translate("AUGGCCAUUGUAAUGGGCCGCUGA"),
            "MAIVMGR"
        )


class TestFindMotif(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(find_motif("GATCGATC", "CGA"), [3])

    def test_overlapping_matches(self):
        self.assertEqual(find_motif("GATATATGCATATACTT", "ATAT"), [1, 3, 9])

    def test_no_match(self):
        self.assertEqual(find_motif("GATCGATC", "TTTT"), [])

    def test_motif_equals_sequence(self):
        self.assertEqual(find_motif("ATCG", "ATCG"), [0])


class TestFindOrfs(unittest.TestCase):
    def test_single_orf(self):
        self.assertEqual(find_orfs("XXATGAAATAGXX"), ["ATGAAATAG"])

    def test_two_orfs(self):
        self.assertEqual(
            find_orfs("XXATGAAATAGXXXATGCCCTGAXX"),
            ["ATGAAATAG", "ATGCCCTGA"]
        )

    def test_no_start_codon(self):
        self.assertEqual(find_orfs("CCCCCCTAA"), [])

    def test_start_without_reachable_stop(self):
        # ATG present but sequence ends before an in-frame stop codon
        self.assertEqual(find_orfs("XXATGAAACCC"), [])

    def test_out_of_frame_stop_is_skipped(self):
        # "ATGGTAGCTAAATGA" contains the letters "TAG" at position 4,
        # but that's NOT in-frame with the ATG at position 0 (frame
        # positions are 0, 3, 6, 9, 12), so it must be ignored. The ORF
        # should extend all the way to the in-frame TGA at position 12.
        self.assertEqual(
            find_orfs("ATGGTAGCTAAATGA"),
            ["ATGGTAGCTAAATGA"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
