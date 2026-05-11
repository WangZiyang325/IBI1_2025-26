'''
Store the sequence in a variable named 'seq'
Store the target stop codons in a list named 'stop_codons'

Create a memory box 'max_len' starting at 0
Create a memory box 'best_orf' starting empty

Loop through every single position 'i' in the sequence:
    Check if the 3 letters starting at 'i' are 'AUG':
        If YES, start a new loop from 'i', moving 3 steps at a time (index 'j'):
            Extract the 3 letters at 'j'
            If these 3 letters are in 'stop_codons':
                Cut out the whole piece from 'i' to 'j+3'
                If this piece is longer than 'max_len':
                    Update 'max_len' with the new length
                    Update 'best_orf' with the new piece
                Stop the inner loop (we found the first stop sign!)

Print out 'best_orf' and 'max_len
'''


seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop_codons = ['UAA', 'UAG', 'UGA']

max_len = 0
longest_orf = ""

for i in range(len(seq)-2):
    if seq[i:i+3] == 'AUG':
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                current_orf = seq[i:j+3]
                if len(current_orf) > max_len:
                    max_len = len(current_orf)
                    longest_orf = current_orf
                break 

print(f"The longest ORF is: {longest_orf}")
print(f"Length: {max_len} nucleotides")


