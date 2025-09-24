
class KMP:

    '''
    Method learned in CSC226 data structures and algorithms at UVIC
    Taught in a more concrete way by neetcode: https://www.youtube.com/watch?v=JoF0Z7nVSrA&t=225s
    '''

    @staticmethod
    def generate_lps(query_string:str)->list[str]:
        '''
        input: 
            query_string: The string that you would like to search for
        output: 
            a longest-prefix suffix (lps) array


        
        A longest prefix-suffix array tells you how long the longest prefix equal to the suffix is from the 
        start of the query_string to the nth index. In this case prefix and suffix cannot be the entire string from
        0 to the nth index
        '''
        query_string_len = len(query_string)
        lps = [0] * query_string_len
        prevLPS,  curr_query_string_index = 0, 1

        while curr_query_string_index < query_string_len:

            if query_string[curr_query_string_index] == query_string[prevLPS]:
                prevLPS += 1
                lps[curr_query_string_index] = prevLPS

                curr_query_string_index += 1
            else:
                if prevLPS == 0:
                    lps[curr_query_string_index] = 0
                    curr_query_string_index +=1
                else:
                    prevLPS = lps[prevLPS - 1]
        return lps
    

    @staticmethod
    def KMP_search(super_string:str,sub_string:str, find_all:bool=True) -> list[int]:
        '''
        Inputs:
            super_string: A string we are searching within
            sub_string: the string we're looking for within the super_string
            find_all: By default this is true, and results in all positions of the occurence being returned
        Find position(s) of occurence(s) of substring in superstring 
        '''
        lps_arr = KMP.generate_lps(sub_string)
        
        super_string_index, sub_string_index = 0, 0
        super_string_len = len(super_string)
        sub_string_len  = len(sub_string)
        output_arr = []
        while super_string_index < super_string_len:

            if super_string[super_string_index] == sub_string[sub_string_index]:
                super_string_index += 1
                sub_string_index += 1
            elif sub_string_index == 0:
                    super_string_index += 1
            else:
                    sub_string_index = lps_arr[sub_string_index - 1]
            
            if sub_string_index == sub_string_len:
                 output_arr.append(super_string_index - sub_string_len)
                 sub_string_index = 0
                 if not find_all:
                    break

                 # We have found the substring!
                 pass
        
        return output_arr


        pass
    pass