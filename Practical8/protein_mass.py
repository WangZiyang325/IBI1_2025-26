# Practical 8: Protein Mass Predictor
# This function calculates the monoisotopic mass of a protein sequence.

def calculate_protein_mass(sequence):
    """
    Calculate total protein mass from an amino acid sequence.
    Arguments:
        sequence (str): A string of single-letter amino acid codes.
    Returns:
        float: Total mass in atomic mass units (amu).
    Raises:
        ValueError: If an invalid amino acid is provided.
    """
    # Dictionary of amino acid residue masses (monoisotopic, amu)
    aa_masses = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    total_mass = 0.0

    # Loop through each amino acid in the input sequence
    for aa in sequence:
        if aa not in aa_masses:
            raise ValueError(f"Invalid amino acid detected: {aa}")
        total_mass += aa_masses[aa]

    return total_mass

# Example function call
if __name__ == "__main__":
    sample_sequence = "AVPGS"
    try:
        mass = calculate_protein_mass(sample_sequence)
        print(f"Sequence: {sample_sequence}")
        print(f"Total protein mass: {mass:.2f} amu")
    except ValueError as e:
        print("Error:", e)