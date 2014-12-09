#!/usr/bin/env python
import sys
from src.fasta_reader import read_fasta
from src.sequence import Sequence
from src.sequtil import translate

def main():
    if len(sys.argv) < 4:
        print("Usage: unigener.py <input_fasta> <output_prefix> <unigene1> <unigene2> ...")
        exit()

    input_fasta_path = sys.argv[1]
    output_prefix = sys.argv[2]
    unigenes = sys.argv[3:]

    with open(input_fasta_path, 'r') as fasta:
        print("Reading fasta...")
        seqs = read_fasta(fasta)
        isoforms = {}
        print("Sorting isoforms...")
        for seq in seqs:
            for unigene in unigenes:
                if seq.header.startswith(unigene):
                    if unigene not in isoforms:
                        isoforms[unigene] = [seq]
                    else:
                        isoforms[unigene].append(seq)
        print("Writing results...")
        with open(output_prefix+'.fasta', 'w') as out_fasta, open(output_prefix+'.pep', 'w') as out_pep:
            for unigene, seqs in isoforms.items():
                for seq in seqs:
                    out_fasta.write(seq.to_fasta())
                    out_pep.write(Sequence(seq.header, translate(seq.bases, '-')).to_fasta())


###########################################

if __name__ == '__main__':
    main()
