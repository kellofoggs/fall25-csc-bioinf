The DeBruijn Graph based assembler I ported over from Python to Codon assembles shorter reads into list of contigs of decreasing length.

First I cut the reads into k-mers of length k, then I build a De Bruijn graph from these k-mers. Finally, I traverse walk through the graph finding the deepest non-branching paths to output as contigs. After I find a contig, I remove that kmer/nodes that were used to make that contig from the graph, and repeat until a certain number of contigs have been found or the graph is empty.

There are some catches though. The original implementation erroneuously created kmers for the reads. Instead of creating k + n -1 kmers for a read of length n, k+n -2 kmers were created. I replicated this error in the Codon implementation in an attempt to yield similar results for the purposes of the assignment.

In addition the original implementation used a hash set to store children of nodes in the De Bruijn graph as kmers. I used integers as these are faster to compare and hash than strings generally. Because of this when returning a list of children of a node sorted by their number of occurrences, there may be conflicts with the original implementation's results if two kmers have the same number of occurrences as the initial position of these kmers in the hash set is determined by a hash function for strings rather than the integer index I used. There is also no guaranteeing that the same hash function is used for strings across the different implementations. This may be why some of my results differ from the original implementation.

When looking for the organisms that the contigs came from, I used BLAST to search against the proper graph instead of the graph formed by k + 1 -2 kmers per read. This yielded better results, as the longest contigs were longer and more specific to the organisms they came from.

The most likely results were as follows:
|Data file| Organism | Number of Contigs | Longest Contig Length | Percentage of Contigs |
|---------|----------|-------------------|-----------------------|-----------------------|


Potential improvements:
* Iteratively DFS instead of recursively DFS to avoid stack overflow on larger graphs from function calls being added to the call stack. 

