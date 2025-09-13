from Utilities.InputFileTools import Fasta, GenericTextFile
from typing import Union, Dict, List
import argparse
class BaseSolution:
    parser:argparse.ArgumentParser = None
    file_name:str = None
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-f',"--file", help="Path to the file (full or relative) that the script reads in as input")
        args = self.parser.parse_args()
        
        self.file_name = args.file

        pass

    
    def get_fasta_input_file(self, as_dict:bool=False) -> Union[List[str], Dict[str,str]]:
        '''
        Opens the provided input file and returns it's contents either as a list of DNA strings, or as a dictionary
        where the values are dna strings and the keys are the ids of the dna strings
        '''

        with open(self.file_name)  as input_file :
            if as_dict:
                return Fasta.get_fasta_as_dict(input_file)
            else:
                return Fasta.get_fasta_as_list(input_file)
    
    def get_generic_input_file(self, as_str:bool=False) -> Union[List[str], str]:
        with open(self.file_name)  as input_file :
            if as_str:
                return GenericTextFile.get_generic_file_as_str(input_file)
                pass
            else:
                return GenericTextFile.get_generic_file_as_lines(input_file)
                pass
            

        pass
