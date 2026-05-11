# Define input and output file paths
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fasta = "stop_genes.fa"

# Define start and stop codons for DNA sequence
start_codon_dna = "ATG"
stop_codons_dna = ["TAA", "TAG", "TGA"]

# Parse FASTA file and store genes in a dictionary
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
                # Extract gene name from header
                current_name = line.split()[0][1:]
                current_seq = ""
            else:
                # Concatenate sequence lines
                current_seq += line.upper()
        # Save the last gene
        if current_name and current_seq:
            genes[current_name] = current_seq
    return genes

# Check for in-frame stop codons after ATG
def has_inframe_stop(seq):
    found_stops = set()
    for i in range(len(seq)-2):
        if seq[i:i+3] == start_codon_dna:
            # Read codons in frame
            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons_dna:
                    found_stops.add(codon)
                    break
    return sorted(list(found_stops)) if found_stops else None

# Main workflow: parse, filter, and write filtered FASTA
if __name__ == "__main__":
    gene_dict = parse_fasta(input_fasta)
    
    with open(output_fasta, "w") as out_f:
        for gene_name, sequence in gene_dict.items():
            stop_list = has_inframe_stop(sequence)
            if stop_list:
                # Write new header with stop codon information
                header = f">{gene_name} stop={','.join(stop_list)}"
                out_f.write(header + "\n")
                out_f.write(sequence + "\n")
    
    print("Filtering complete. Output saved to stop_genes.fa")