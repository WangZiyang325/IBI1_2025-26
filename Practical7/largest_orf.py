# Define the input mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Define the list of stop codons
stop_codons = ['UAA', 'UAG', 'UGA']

# Initialize variables to store the longest ORF and its length
max_len = 0
longest_orf = ""

# Iterate through the sequence to find start codon AUG
for i in range(len(seq)-2):
    if seq[i:i+3] == 'AUG':
        # Scan codons in frame starting from AUG
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            # Check if current codon is a stop codon
            if codon in stop_codons:
                current_orf = seq[i:j+3]
                # Update the longest ORF if current one is longer
                if len(current_orf) > max_len:
                    max_len = len(current_orf)
                    longest_orf = current_orf
                break 

# Output the result: handle both found and not found cases
if max_len == 0:
    print("No valid ORF found in the sequence.")
else:
    print(f"The longest ORF is: {longest_orf}")
    print(f"Length: {max_len} nucleotides")