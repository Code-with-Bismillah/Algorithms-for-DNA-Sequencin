from parser import read_fastq
from graph import build_overlap_graph

def main():
    filepath = "data/ERR266411_1.for_asm.fastq"
    reads = read_fastq(filepath)
    print(f"Total reads: {len(reads)}")

    k = 30
    graph = build_overlap_graph(reads, k=k)

    edge_count = sum(len(v) for v in graph.values())
    node_count = len(graph)
    print(f"Graph Summary:")
    print(f"  Nodes with edges: {node_count}")
    print(f"  Total edges: {edge_count}")

if __name__ == "__main__":
    main()
