# tests/test_parser.py

from src.parser import read_fastq

def test_read_fastq():
    reads = read_fastq("data/test.fastq")
    assert len(reads) > 0
