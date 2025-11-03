
# A class for opening and interpreting fasta files, I got tired of rewriting the same function
# from io import TextIO
import re

class Fasta:
    # Class for handling the fasta format, can use either a raw fasta string or a file handle as input or the file's path


    @staticmethod
    def get_fasta_as_dict(fasta_string: str) -> dict:   
    # def get_fasta_as_dict(fasta: Union[TextIO, str]) -> dict:   

        matches_list = re.split(">(.*)", fasta_string)[1:] # Skip the blankspace match, this is not necessary if I just used re.finditer
        sequence_labels = list(map(str.strip,matches_list[::2] ))
        sequence_list = list(map(lambda sequence: re.sub(r"\s", "", sequence), matches_list[1::2]))

        id_to_sequence_dict = dict(zip(sequence_labels, sequence_list))

        return id_to_sequence_dict

    @staticmethod
    def get_fasta_as_list(fasta_string: str) -> list:   
    # def get_fasta_as_list(fasta_file: Union[TextIO, str]= None, fasta_string= None) -> dict:   

        # if fasta_string is not None:
        #     string = fasta_string
        # else:
        #     if type(fasta_file) == TextIO:
        #         string = fasta_file.read()
        #     elif type(fasta_file) == str:
        #         with open(fasta_file) as f_file:
        #             string = f_file.read()

        matches_list = re.split(">(.*)", fasta_string)[1:] # Skip the blankspace match

        
        sequence_list = list(map(lambda sequence: re.sub(r"\s", "", sequence), matches_list[1::2]))
        
        return sequence_list
    
    # @staticmethod
    # def write_fasta_to_file(fasta_string_name_list:list[str], fasta_content_list:list[str], file_path: str,do_append:bool = False):
    #     if (len(fasta_string_name_list) != len(fasta_content_list)) or len(fasta_string_name_list) < 1:
    #         raise ValueError("The fasta_string_list and fasta_content_list should be equal in length, and neither should be empty")
    #     open_flag = 'a' if do_append else 'w'
    #     with open(file_path, open_flag) as file:
    #         for fasta_label fasta_
    #         pass    

    #     pass


class GenericTextFile:
    '''
    Used to convert fasta file into different formats, pass in the file path or file handle
    '''
    @staticmethod
    def get_generic_file_as_lines(file: str, is_binary_file:bool=False) -> list[str]:
        perm_flag = 'rb' if is_binary_file else 'r'
        if type(file) == str:
            with open(file, perm_flag) as text_file:
                return text_file.read().splitlines()
        
        # elif type(file) == TextIO:
        #     return file.read().splitlines()
        #     pass
        else:
            raise Exception("Either pass in the fast file as a string that is it's file path or a TextIO object")
    
    @staticmethod 
    def get_generic_file_as_str(file: str, is_binary_file:bool=False) -> str:
            perm_flag = 'rb' if is_binary_file else 'r'

            if type(file) == str:
                with open(file, perm_flag) as text_file:
                    return text_file.read()
                
            # elif type(file) == TextIO:
            #     return file.read()
            else:
                raise Exception("Either pass in the fast file as a string that is it's file path or a TextIO object")
    