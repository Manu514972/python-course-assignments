import sys
from collections import Counter

codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

codon_to_aa = {codon: aa for aa, codons in codon_table.items() for codon in codons}

def count_amino_acids(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            sequence = ''.join(line.strip() for line in lines if not line.startswith('>')).upper()

        amino_acid_counts = Counter()
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if len(codon) == 3:
                aa = codon_to_aa.get(codon, 'Unknown')
                amino_acid_counts[aa] += 1

        for aa, count in amino_acid_counts.items():
            print(f"{aa}: {count}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids.py <fasta_file>")
    else:
        count_amino_acids(sys.argv[1])
