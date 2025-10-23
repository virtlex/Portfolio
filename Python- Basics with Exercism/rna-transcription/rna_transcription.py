def to_rna(dna_strand):
    new_dna = ""
    for c in dna_strand:
        if c == "G":
            new_dna += "C"
        if c == "C":
            new_dna += "G"
        if c == "T":
            new_dna += "A"
        if c == "A":
            new_dna += "U"
    return new_dna
