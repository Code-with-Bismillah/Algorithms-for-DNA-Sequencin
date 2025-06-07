# tests/test_overlap.py

from src.overlap import overlap

def test_overlap():
    assert overlap("CGTAC", "ACGTA", 2) == 2
    assert overlap("AAAT", "AATG", 3) == 3
    assert overlap("ACGT", "TGCA", 2) == 1
