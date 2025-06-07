# Compute minimum edit distance between a pattern and all reads in a FASTQ file
from parser import read_fastq

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def read_fasta(filename):
    """Reads a FASTA file and returns the concatenated sequence as a single string."""
    seq = []
    with open(filename) as f:
        for line in f:
            if line.startswith('>'):
                continue
            seq.append(line.strip())
    return ''.join(seq)

if __name__ == "__main__":
    sequence = read_fasta("data/chr1.GRCh38.excerpt.fasta")
    patterns = [
        "GCTGATCGATCGTACG",
        "GATTTACCAGATTGAG"
    ]
    for pattern in patterns:
        min_dist = float('inf')
        for i in range(len(sequence) - len(pattern) + 1):
            window = sequence[i:i+len(pattern)]
            dist = edit_distance(pattern, window)
            if dist < min_dist:
                min_dist = dist
        print(f"Pattern: {pattern}, Min Edit Distance: {min_dist}")
