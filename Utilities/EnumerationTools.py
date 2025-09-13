
from typing import List
from itertools import product

class Enumerations:
    @staticmethod
    def fast_lex_words(alphabet:List[str], word_length:int):
        return [''.join(p) for p in product(alphabet, repeat=word_length)]



    @staticmethod
    def make_lexographic_strings(alphabet_list:List[str], enum_length=2)->List[str]:


        if enum_length == 1:
            return alphabet_list

        enumeration = Enumerations.make_string_recur(alphabet_list,alphabet_list, count=enum_length, current_layer=0)

        return enumeration

    @staticmethod
    def make_string_recur(prev_layer:List,base_layer:List, count=0, current_layer=0):

        
        if current_layer == count - 1:
            return prev_layer
        
        # prev_layer = []
        curr_layer = []
        for i in range(0, len(prev_layer)):
            for j in range(0, len(base_layer)):
                curr_layer.append(prev_layer[i] + base_layer[j])


        next_layer = Enumerations.make_string_recur(curr_layer ,base_layer, count, current_layer+1)
        
        return next_layer
    @staticmethod
    def make_var_len_lex_strings(alphabet_list:List[str], max_len:int):
        
        pass