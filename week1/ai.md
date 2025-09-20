AI Resposes/prompts are generated with OpenAI GPT-5

1. Translate this document into english for me:

2. For the translated pdf I want you to translate it and return a pdf for me to read.

3. Is this valid: {actions.yaml}

4. In relations to actions.yaml: 
 * What does check out repository code do then?
 * Can there only be one uses statement under each name?
 * Can steps be under name?
 
5. Is there anyway to setup a path in something like a makefile for codon?
Explanation: I wanted chatgpt to help me figure out if theres a way to setup something like a PYTHONPATH for resolving imports cleanly. 
6. Codon union already sealed {dna.py source code}
Explanation: I previously wrote a method that can take in a fasta filehandle or the contents of a fasta file in a string. I could not find what type codon considered file handles and opted to only allow the method to deal with strings. 

7. InputFileTools.py:14 (9-69): error: 'List[str]' does not match expected type 'List[Optional[str]]' -> Codon does not have typing

Explanation: I tried to get chatgpt to help me figure out why my codon code was not compiling. It said I should import the typing library. The fix was to remove the Optional paramater as theres no need to include a "None" type in the list I wanted to use.

8. 
