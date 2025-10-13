This week I started off with tests instead of with the source code as that was what caused me trouble last week. As Codon does not have an extensive standard library or package manager (especially compared to something like Python) I again used the @test annotation to create tests for the phylo tree modules. These tests covered neighbor-joining and UPGMA algorithms, as well as tree node distance calculations. By going off the tests, I was able to better understand the requirements the code needed to fulfill. 

# Steps
The cython syntax doesn't really complicate much as cython is also based on python much like Codon. The static typing in Cython made it easier to figure out what types to use in Codon. The professor provided hints for fixes to the some of the issues with Codon. For example Codon does not support some collections like Frozenset, so an extended version of the set class from the standard library was provided. This is an example of how to extend a class in Codon, which is currently missing from the documentation.



# Gripes 

## Newick format
###  **Disclamer**: This section is a short rant about the newick tree format and how much I dislike it. If you don't care about that, skip to the next section.

The newick format is yet another example of one of the many file formats in bioinformatics that I really dislike. It's used to represent trees in a text format in a very compact way. However this format is not very readable and it is very easy to make mistakes when writing or reading newick files. There are also a lot of different variations of the newick format which makes it even more confusing. There are great newer tree formats out there like Nexus and PhyloXML that are much more readable and easier to work with. I really don't understand why newick is still so widely used in the bioinformatics community for new projects.

 I would honestly prefer to write a tree in graphviz format over newick any day. Building a parser for newick files is also a pain as there are so many edge cases to consider. Overall, I think the newick format is a bad choice for representing trees and I would love to see it replaced by a better format in the future.

It's understandble that newick is used for compactness, but with today's storage capabilities I don't think that is really a valid argument anymore. I do recognize that lots of legacy systems utilize this format, but I hope that one day we'll be past this format.
**Rant over**

## Compiled Language Blues
There is a small amount of overhead when converting from a dynamic language to a static one. For instance in my from_newick function in my Node class I originally had a ternary operator to check if a label_list was empty/None and to assign an index to a value that matched the label if the label could be found in the labels_list. Now this is a very pythonic way of doing this but leaves some unresolved edge cases that I had to handle with a for loop, nested within multiple if statements. This made the code less readable and more complex than I would have liked which I think is a strength of Python. Alternatively I could have tried to hand this part of the code off to a python script, but I wanted to keep the code in Codon as much as possible. Perhaps there are guidlines for handling such cases in Codon that I am not aware of yet.

# Positives
I really enjoyed how the original implementation had detailed and well thought out comments/docstrings especially when it came to parsing newick trees. I liked the examples they gave for function/class usage but did not like the naming scheme for a lot of the variables. Some variables also were never actually used which I found rather strange, although I did not remove them from my implementation. I'm interested to see how/if Codon will integrate other major python libraries/packages in the future such as pandas or if this is something better off used with the python bindings Codon provides.

# Concerns
In the original implementation there are portions of the codebase that are not covered by the tests I ported over such as the "as_graph()" function. I also was thinking about how a class can reference a member of the same class in its definition. For example, in the Node class, a Node can have a parent which also a Node object. In the official documentation it says to wrap the class in an Optional[]. This worked for me but I did not have to do this when I had a list of children Nodes. Instead I was able to use list[Node]. I'm not sure why this is the case and if this is a bug or intended behavior. Also indicating the optionality of a variable ended up being a bit of a hassle when comparing variables but ended up promoting good coding practices such as checking for None before using a variable.

Results:
Running the following tests for the phylo package using both python and codon yield the following results:

