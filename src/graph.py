# src/graph.py

from overlap import overlap

def build_kmer_dict(reads, k):
    """Index all k-mers to reads containing them."""
    kmer_dict = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            kmer_dict.setdefault(kmer, set()).add(read)
    return kmer_dict

def build_overlap_graph(reads, k):
    """Builds a directed graph based on suffix-prefix overlaps."""
    index = build_kmer_dict(reads, k)
    graph = {}
    for read in reads:
        suffix = read[-k:]
        if suffix in index:
            for other in index[suffix]:
                if read != other:
                    olen = overlap(read, other, k)
                    if olen > 0:
                        graph.setdefault(read, []).append((other, olen))
    return graph
