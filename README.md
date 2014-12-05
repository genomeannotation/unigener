unigener is an amazing product which causes a transcriptome assembly to open itself like a flower before your eyes. Here is an example of its awesome power:

    > python3 unigener.py fasta=sample_data/sample_transcriptome.fasta unigenes=c20385_g1 outprefix=c20385_g1.unigenes

Running that exciting command will net you not one but *two* fascinating output files -- c20385_g1.unigenes.fasta and c20385_g1.unigenes.pep.

As you might expect, the former is a fasta of all isoforms of unigene c20385_g1, and the latter is the amino acid sequences corresponding to the same.

But wait there's more. You can provied unigener with a list of unigenes and get a bigger, better fasta:

    > python3 unigener.py fasta=sample_data/sample_transcriptome.fasta unigenes=c20385_g1,c18809_g1 outprefix=my_cool_unigenes

This command will give you two files, my_cool_unigenes.fasta and my_cool_unigenes.pep. Each will contain all isoforms for the two unigenes c20385_g1 and c18809_g1.

unigener will make all your wildest dreams come true.
