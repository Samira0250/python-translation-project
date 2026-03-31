#! /usr/bin/env python3

import sys
from find_orf import find_first_orf, parse_sequence_from_path
from translate import translate_sequence

def main():
    import argparse

    default_start_codons = ['AUG']
    default_stop_codons  = ['UAA', 'UAG', 'UGA']

    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    parser = argparse.ArgumentParser(
        description='Find and translate the first ORF in a nucleotide sequence.')

    parser.add_argument('sequence',
                        metavar='SEQUENCE',
                        type=str,
                        help='The sequence to search.')
    parser.add_argument('-p', '--path',
                        action='store_true',
                        help='Treat sequence argument as a file path.')
    parser.add_argument('-s', '--start-codon',
                        type=str,
                        action='append',
                        default=None,
                        help='A start codon (can be used multiple times).')
    parser.add_argument('-x', '--stop-codon',
                        type=str,
                        action='append',
                        default=None,
                        help='A stop codon (can be used multiple times).')

    args = parser.parse_args()

    if args.path:
        sequence = parse_sequence_from_path(args.sequence)
    else:
        sequence = args.sequence

    if not args.start_codon:
        args.start_codon = default_start_codons
    if not args.stop_codon:
        args.stop_codon = default_stop_codons

    orf = find_first_orf(sequence=sequence,
                         start_codons=args.start_codon,
                         stop_codons=args.stop_codon)

    if orf:
        peptide = translate_sequence(orf, genetic_code)
        sys.stdout.write('{}\n'.format(peptide))
    else:
        sys.stdout.write('No ORF found\n')

if __name__ == '__main__':
    main()
