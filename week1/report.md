### Report Author: Kelly Ojukwu
### Report Title: Week 1 Report - Porting over a DeBruijn Graph Assembler in Codon to improve performance.

## Methodology:
The DeBruijn Graph based assembler I ported over from Python to Codon assembles shorter reads into list of contigs of decreasing length. The python implementation I used as a reference is created by Chen Zhongyu's implementation and hosted on github: https://github.com/zhongyuchen/genome-assembly

First I cut the reads into k-mers of length k, then I build a De Bruijn graph from these k-mers. Finally, I traverse walk through the graph finding the deepest non-branching paths to output as contigs. After I find a contig, I remove the kmer/nodes that were used to make that contig from the graph, and repeat until a certain number of contigs have been found or the graph is empty.

## Caveats
There are some catches though. The original implementation erroneuously created kmers for the reads. Instead of creating k + n -1 kmers for a read of length n, k+n -2 kmers were created. I replicated this error in the Codon implementation in an attempt to yield similar results for the purposes of the assignment.

In addition the original implementation used a hash set to store children of nodes in the De Bruijn graph as kmers. I used integers as these are faster to compare and hash than strings generally. Because of this when returning a list of children of a node sorted by their number of occurrences, there may be conflicts with the original implementation's results if two kmers have the same number of occurrences as the initial position of these kmers in the hash set is determined by a hash function for strings rather than the integer index I used. There is also no guaranteeing that the same hash function is used for strings across the different implementations. This may be why some of my longest contigs differ from the original implementation, as choosing a different contig of equal length as another may lead to a different path being taken through the graph later on as there is no replacement for nodes removed after path traversal/contig creation.

## Results:

Across all four data sets the codon impplementation was significantly faster than the python implementation, without sacrificing N50 score ( an assembly quality KPI where a higher N50 across the same sample and different assemblers is often preferred. This metric is not the end-all-be-all). 

The results are as follows:

Dataset         Language        Runtime         N50            
----------------------------------------------------------------
data1           python          0:00:16         9990           
data1           codon           0:00:07         9990           
data2           python          0:00:34         9992           
data2           codon           0:00:17         9992           
data3           python          0:00:39         9824           
data3           codon           0:00:17         9824           
data4           python          0:07:39         159255         
data4           codon           0:03:11         159255         

The codon implementation was on average approximately 100% faster than the python implementation across all four datasets. The N50 score was identical across both implementations for all four datasets.

When looking for the organisms that the contigs came from, I used BLAST to search against the proper graph instead of the graph formed by k + 1 -2 kmers per read. This yielded better results, as the longest contigs were longer and more representative of the reads in the sample.


A note about blastn: I used the online tool BLAST (specifically blastn for nucleotide alignment)  to search for places in known genomes that the contigs match. I have included both E-values which can be interpreted as the probability that the sequences would occur in the genome by random chance. A lower E-Value implies that a match is more likely with that specific organism. Of course because the database has different readings from different chromosomes listed seperately for organisms of the same species, it's best to look at the species with the lowest E-values, high percent identity, and high total score.
The most likely results are as follows as determined by the previous criteria:

## BLAST Organism Search Results



|Data file| Organism | Number of Contigs put through BLAST| Longest Contig put through BLAST Length | E-value of Highest Coverage Genome-ContigList pair for organism|
|---------|----------|-------------------|-----------------------|-----------------------|
|Data file 1 (codon-revised)| Porphyromonas gingivalis| 20 | 15651| 0.0| 
|Data file 2 (codon-revised)| Porphyromonas gingivalis| 20 | 15745| 0.0| 
|Data file 3 (codon-revised)| Parabacteroides distasonis| 20 | 9825| 0.0|
|Data file 4 (codon-revised)| Prevotella melaninogenica | 15 | 27999| 0.0|

Note: Because Data file 4 was so massive in contig length, I lowered the number of contigs put into the BLAST search to 10 instead of 20 to reduce the time taken for the search. Initially I ran into an error where the BLAST search could not be completed because the process size was too large. Instead of using the largest 20 contigs, I used the list of the largest 20 contigs and took a slice of this list from index 5 (in zeror based indexing) to the end of this list. This yielded a list of 15 contigs that were still large, but not as large as the original 20 contigs and allowed the process to actually finish



## Usage:
To use the assembler load each read in the fasta file format into its own child directory of your naming. Then compile the assembler with codon build -release ~/path/to/repo/week1/main.codon -o assembler. Then run the assembler with ./assembler ~/path/to/data/file. Feel free to tweak the kmer size in the main.codon script prior to compiling, the default k is 25. If you would like to use the correct implementation of kmer generation, comment out the following line from dbg.codon:
``` 
for curr_kmer in list(DNAStringTools.generate_kmers(read, k))[:-1]:
```

and uncomment this line:
```
for curr_kmer in list(DNAStringTools.generate_kmers(read, k)):
```

The assembler will output a list of contigs in a file named contigs.fasta in the same directory that your data file is in. The contigs will be sorted from longest to shortest. You can tweak the number of contigs output by changing the num_contigs variable in main.codon. The default is 20.


## Potential improvements:
* Iteratively DFS instead of recursively DFS to avoid stack overflow on larger graphs from function calls being added to the call stack. 
* Use smaller ints for idx to conserve memory
* store graph as a list of edge objects where repeat edges are represented as 
* Add support for arguments to change kmer size and number of contigs to output instead of editing source code.