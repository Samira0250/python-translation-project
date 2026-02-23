#! /usr/bin/env python3

import sys


def translate_sequence(rna_sequence, genetic_code):
    rna_sequence = rna_sequence.upper()
    protein = ""

    if len(rna_sequence) < 3:
        return ""

    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]

        if codon not in genetic_code:
            continue

        amino_acid = genetic_code[codon]

        if amino_acid == "*":
            break

        protein += amino_acid

    return protein


def get_all_translations(rna_sequence, genetic_code):
    rna_sequence = rna_sequence.upper()
    peptides = []

    for i in range(len(rna_sequence) - 2):
        if rna_sequence[i:i+3] == "AUG":
            peptide = translate_sequence(
                rna_sequence=rna_sequence[i:],
                genetic_code=genetic_code
            )
            if peptide:
                peptides.append(peptide)

    return peptides


def get_reverse(sequence):
    sequence = sequence.upper()
    return sequence[::-1]


def get_complement(sequence):
    sequence = sequence.upper()

    complement = {
        "A": "U",
        "U": "A",
        "G": "C",
        "C": "G"
    }

    result = ""
    for base in sequence:
        result += complement.get(base, "")

    return result


def reverse_and_complement(sequence):
    return get_complement(get_reverse(sequence))


def get_longest_peptide(rna_sequence, genetic_code):
    peptides = []

    # forward strand
    peptides += get_all_translations(rna_sequence, genetic_code)

    # reverse complement strand
    rev_comp = reverse_and_complement(rna_sequence)
    peptides += get_all_translations(rev_comp, genetic_code)

    if not peptides:
        return ""

    return max(peptides, key=len)


if __name__ == '__main__':
    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}

    rna_seq = ("AUG"
               "UAC"
               "UGG"
               "CAC"
               "GCU"
               "ACU"
               "GCU"
               "CCA"
               "UAU"
               "ACU"
               "CAC"
               "CAG"
               "AAU"
               "AUC"
               "AGU"
               "ACA"
               "GCG")

    longest_peptide = get_longest_peptide(
        rna_sequence=rna_seq,
        genetic_code=genetic_code
    )

    assert isinstance(longest_peptide, str)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
        rna_seq,
        longest_peptide)
    sys.stdout.write(message)

    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
