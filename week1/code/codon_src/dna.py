
from collections import Counter
from search import KMP
class DNAStringTools:



    '''
    Class with static methods used for handling common DNA tasks such as 
    converting DNA codons to amino acids and reverse complementing dna
    
    Also 
    '''

    # dna_nuc_complement_trans = str.maketrans({"A": "T", "T": "A", "G": "C", "C":"G"})
    dna_nuc_complement_dict = {"A": "T", "T": "A", "G": "C", "C":"G"}
#     _dna_codon_table_string = '''TTT F      CTT L      ATT I      GTT V
# TTC F      CTC L      ATC I      GTC V
# TTA L      CTA L      ATA I      GTA V
# TTG L      CTG L      ATG M      GTG V
# TCT S      CCT P      ACT T      GCT A
# TCC S      CCC P      ACC T      GCC A
# TCA S      CCA P      ACA T      GCA A
# TCG S      CCG P      ACG T      GCG A
# TAT Y      CAT H      AAT N      GAT D
# TAC Y      CAC H      AAC N      GAC D
# TAA Stop   CAA Q      AAA K      GAA E
# TAG Stop   CAG Q      AAG K      GAG E
# TGT C      CGT R      AGT S      GGT G
# TGC C      CGC R      AGC S      GGC G
# TGA Stop   CGA R      AGA R      GGA G
# TGG W      CGG R      AGG R      GGG G 
# '''


    dna_codon_to_amino_acid = dict(
    zip(*(iter('''TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G'''.split()),) * 2
    )
)
   # Convert our string into a dictionary of dna to codon translations
    stop_codons = set(["TAA", "TAG", "TGA"])
    start_codons = set(["ATG"]) # "ATG" aka methionine is the most commonly seen start codon although others do exist. For the purposes of this we will assume


    @staticmethod
    def reverse_dna(dna_string:str):
        return dna_string[::-1]
    @staticmethod
    def complement_dna(dna_string:str):
        '''Complements a DNA string, if a char is not a DNA char (A,T,C,G), the original char is not replaced'''
        return "".join(DNAStringTools.dna_nuc_complement_dict.get(char, char) for char in dna_string.upper())

    @staticmethod
    def reverse_complement_dna(dna_string):
        return DNAStringTools.reverse_dna(DNAStringTools.complement_dna(dna_string))
    
    @staticmethod
    def translate_dna_to_amino_acid(dna_string:str):
        output = ""
        for i in range(0, (len(dna_string)//3)):
            codon = dna_string[3*i: 3*i + 3]
            if codon not in DNAStringTools.stop_codons:
                output = output + DNAStringTools.dna_codon_to_amino_acid[codon] 
            else:
                break
        return output   

    @staticmethod
    def to_RNA(dna_strand:str) -> str:
        '''
        Convert a DNA strand string to an RNA strand string by replacing T with U
        '''
        return dna_strand.replace("T", "U")

    @staticmethod
    def count_nucleoutides(dna_string:str):
        return Counter(dna_string)
    
    @staticmethod
    def combine_strings(string_one:str, string_two:str, overlap_threshold:int=None) -> str:
        ''' The dataset is guaranteed to satisfy the following condition: there exists a unique way to 
        reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by
        more than half their length.

        This means that if over half of the second string is in the first we string we combine them and are guaranteed to get the correct combination
        '''

        """
        What we want to do is look at the second half of the first string and see where 
        it has the same ordered chars as the first half of the second string
        We're trying to find the point in string one where the most of the first half of string two can reside
        """
        
        s_one_len = len(string_one)

        s_two_len = len(string_two)
        if overlap_threshold is None:
            overlap_threshold = min(s_one_len//2, s_two_len//2)


        # What we want to do is see how much of the suffix of the first string overlaps with the prefix of the second string
        # If the overlap is past our overlap threshold, we can combine the two strings
        # Else we will return None

        num_overlap_chars = DNAStringTools.find_max_overlaps(string_one, string_two)

        if num_overlap_chars > overlap_threshold:
            output = string_one + string_two[num_overlap_chars:]
            return output
        elif overlap_threshold == 0:
            return string_one+string_two
        else:
            return None
        
    @staticmethod
    def find_max_overlaps(prefix_string, suffix_strings:str) -> int:
        ''' Take in a prefix string, and list of suffix strings
            Return the maximum overlap between the two strings 
            
        '''

        # We will use the lps borrowed from the KMP algorithm to find the maximum overlap between the two strings
        # If we construct a string that is the second string + <a_char_we_know_is_outside_the alphabet of the two strings)> + the first string
        # We can use the lps array to find the maximum overlap between the two strings (as the lps array will tell us how many characters match between the
        # prefix of the second string and the suffix of the first string)

        combined_strings = f'{suffix_strings}#{prefix_string}'
        max_overlap = KMP.generate_lps(combined_strings)[-1]  # The last value in the lps array will tell us the maximum overlap between the two strings
        return max_overlap
    
    @staticmethod
    def find_dna_difference_locs(dna_string_one, dna_string_two, is_greedy_search:bool= False):
        string_one_len = len(dna_string_one)
        string_two_len = len(dna_string_two)
        difference_locs = []
        if string_one_len == string_two_len:
            for i in range(0, string_one_len):
                if dna_string_one[i] != dna_string_two[i]:
                    difference_locs.append(i)
                    if is_greedy_search:
                        return difference_locs
        else:
            raise IOError(f"String lengths must be equal to use this method. String one has length: {string_one_len}, string two has length: {string_two_len}")
        return difference_locs

    @staticmethod
    def count_point_mutations(dna_string_one, dna_string_two):
        string_one_len = len(dna_string_one)
        string_two_len = len(dna_string_two)
        diff = 0
        if string_one_len == string_two_len:
            for i in range(0, string_one_len):
                if dna_string_one[i] != dna_string_two[i]:
                    diff = diff + 1
        else:
            raise IOError(f"String lengths must be equal to use this method. String one has length: {string_one_len}, string two has length: {string_two_len}")

        return diff

    @staticmethod
    def generate_kmers(dna_string: str, k:int) -> Generator[str]: # type: ignore
        '''
        Generate kmers of length k for a given dna_string with a generator. This avoids having to store all the kmers in memory at once.
        Args:
            dna_string (str): The dna string to generate kmers from
            k (int): The length of the kmers to generate
        
        Returns:
            A list of k-mers
        '''

        dna_string_len = len(dna_string)
        if not k > 0 or type(k) is not int:
            raise ValueError(f"k has a value of {k} and is of type {type(k)}, k must be a positive integer")
        elif k > dna_string_len:
            raise ValueError(f"k must be less than or equal to the length of the dna string passed. String length: {dna_string_len}, K value: {k}")
        else:
            num_kmers = dna_string_len - k + 1
            for i in range(num_kmers):
                yield dna_string[i:i+k]

        


            


class ProbabilityTools:

    @staticmethod
    def caclulate_dna_probability(gc_content:float, dna_string:str):
        '''Calculate the probability of the dna string occuring given GC content'''
        
        nuc_counts = DNAStringTools.count_nucleoutides(dna_string)

        

        prob_dict = ProbabilityTools.calculate_nuc_probs_from_GC(gc_content)
        out_prob = 1
        A = nuc_counts["A"]
        T = nuc_counts["T"]
        G = nuc_counts["G"]
        C = nuc_counts["C"]
        return (prob_dict.get("A")**(A+T)) * (prob_dict.get("G")**(C+G))
        # for char in dna_string:
        #     prob = prob_dict.get(char)
        #     if prob is None and type(prob) not in {float,Decimal}:
        #         raise IOError("The dna string contains non-dna characters")
        #     else: # I know the else isn't necessary it's for readability
        #         out_prob = out_prob * prob

        return out_prob
        pass

    @staticmethod
    def calculate_nuc_probs_from_GC(gc_content:float) -> dict[str, float]:
        '''
        Calculate the probability of each nucleotide occuring based on the GC content.
        @param: gc_content: percentage/float that represents the amount of the string that is either guanine or cytosine
        @return: A dictionary where 
             Each key is the letter that represents the nucleotide in {A,T,G,C} 
             Each value is the float that represents the probability of the nucleotide occuring
        '''

        prob_guanine = prob_cytosine = gc_content/2
        prob_adenine = prob_thymine = (1-gc_content)/2
        return {
            "A": prob_adenine,
            "T": prob_thymine,
            "G": prob_guanine,
            "C": prob_cytosine

        }
        
