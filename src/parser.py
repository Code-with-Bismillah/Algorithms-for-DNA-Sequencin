# src/parser.py

def read_fastq(filename):
    """Reads sequences from a FASTQ file."""
    sequences = []
    with open(filename, 'r') as file:
        while True:
            file.readline()         # Line 1: name (@...)
            seq = file.readline()   # Line 2: sequence
            file.readline()         # Line 3: +
            file.readline()         # Line 4: quality
            if not seq:
                break
            sequences.append(seq.strip())
    return sequences
