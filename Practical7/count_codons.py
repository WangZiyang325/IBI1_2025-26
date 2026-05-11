# Import required libraries for plotting and counting
import matplotlib.pyplot as plt
from collections import Counter

# Define file path and codon parameters
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
start_codon_dna = "ATG"
all_stop_codons = ["TAA", "TAG", "TGA"]

# Reusable FASTA parsing function (same as previous script)
def parse_fasta(file_path):
    genes = {}
    current_name = ""
    current_seq = ""
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_name and current_seq:
                    genes[current_name] = current_seq
                current_name = line.split()[0][1:]
                current_seq = ""
            else:
                current_seq += line.upper()
        if current_name and current_seq:
            genes[current_name] = current_seq
    return genes

# Find longest ORF with specified stop codon, return upstream codons
def get_longest_orf_codons(seq, target_stop):
    longest_codons = []
    max_len = 0
    # Iterate all potential ATG start positions
    for i in range(len(seq)-2):
        if seq[i:i+3] == start_codon_dna:
            codons = []
            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                codons.append(codon)
                # Stop when target stop codon is found
                if codon == target_stop:
                    break
            # Keep only ORFs ending with the target stop codon
            if codons and codons[-1] == target_stop:
                if len(codons) > max_len:
                    max_len = len(codons)
                    longest_codons = codons[:-1]  # Exclude the stop codon itself
    return longest_codons

# Main execution
if __name__ == "__main__":
    # Get valid stop codon input from user
    while True:
        user_stop = input("Enter stop codon (TAA/TAG/TGA): ").upper()
        if user_stop in all_stop_codons:
            break
        print("Invalid input! Please enter one of TAA/TAG/TGA")

    # Parse FASTA file
    gene_dict = parse_fasta(input_fasta)

    # Collect all valid codons
    all_codons = []
    for seq in gene_dict.values():
        codons = get_longest_orf_codons(seq, user_stop)
        all_codons.extend(codons)

    # Count codon frequencies
    codon_count = Counter(all_codons)

    # Generate and save pie chart
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
    labels = list(codon_count.keys())
    sizes = list(codon_count.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon Frequency Upstream of {user_stop} (Longest ORF)')
    plt.axis('equal')
    # Save chart as image file
    plt.savefig(f'codon_pie_{user_stop}.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Print results
    print(f"\nCodon counts upstream of {user_stop}:")
    for codon, count in codon_count.items():
        print(f"{codon}: {count}")
    print(f"\nPie chart saved as: codon_pie_{user_stop}.png")