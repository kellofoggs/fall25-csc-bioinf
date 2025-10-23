import re
from datetime import datetime as dt
import math
class Alignment:


    
    pass

class GlobalAlignment:
    mismatch_score: int 
    match_score: int
    gap_score: int
    aligned_sequence_one: str
    aligned_sequence_two: str



    def __init__(self, s_one:str, s_two:str):
        self.mismatch_score = -3
        self.match_score = 3
        self.gap_score = -2

        matrix, as_one, as_two = self.align_sequences(s_one, s_two)
        self.aligned_sequence_one = as_one
        self.aligned_sequence_two = as_two

    
        pass
    
    pass
    def align_sequences(self, s_one, s_two):
        '''
        s_one and s_two are strings to align
        return: a scoring matrix, the first aligned string, the second a lined string as an unpackable in that specific order.
        '''
        s_one_len = len(s_one)
        s_two_len = len(s_two)

        s_one_aligned = []
        s_two_aligned = []

        # Starting score matrix
        scoring_matrix = [[0]*(s_two_len+1) for indices in range(s_one_len +1) ]

        for s_one_index in range(1, s_one_len+1):
            scoring_matrix[s_one_index][0] = self.gap_score * (s_one_index)
        for s_two_index in range(1, s_two_len+1):
            scoring_matrix[0][s_two_index] = self.gap_score * (s_two_index)


        # Walk through the matrix/optimal edge drawing steps
        for s_one_index in range(1, s_one_len+1):

            for s_two_index in range(1, 1+s_two_len):
                diag_step = -math.inf
                

                if s_one[s_one_index-1] == s_two[s_two_index-1]: # When we have a match
                    diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + self.match_score
                else:
                    diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + self.mismatch_score
                
                horiz_step = scoring_matrix[s_one_index][s_two_index-1] + self.gap_score
                vert_step = scoring_matrix[s_one_index-1][s_two_index] + self.gap_score

                scoring_matrix[s_one_index][s_two_index] = max(horiz_step, diag_step, vert_step)


        # Walk back up the graph/matrix starting from the last ele in the matrix
        s_one_index = s_one_len
        s_two_index = s_two_len

        while (s_two_index > 0 or s_one_index > 0):
            # Initialize all steps as min cost / worst possible score
            diag_step = -math.inf
            vert_step = -math.inf
            horiz_step = -math.inf
            
            # Corner check
            if (s_one_index > 0 and s_two_index > 0): # If we're not touching any of the walls and can still make diags, calc the diag score going up to left
                penalty = 0.0
                if s_one[s_one_index - 1] == s_two[s_two_index-1]:
                    penalty = self.match_score
                else:
                    penalty = self.mismatch_score
                diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + penalty            
            vert_step
            
            if s_one_index > 0: # We can travel up still
                vert_step = scoring_matrix[s_one_index-1][s_two_index] + self.gap_score
            if s_two_index > 0: # We can travel left still
                horiz_step = scoring_matrix[s_one_index][s_two_index-1] + self.gap_score

            

            # Check if we have a match (we can take a diagonal)
            if s_one_index  > 0 and s_two_index> 0 and scoring_matrix[s_one_index][s_two_index] == diag_step:
                s_one_aligned.append(s_one[s_one_index - 1])
                s_two_aligned.append(s_two[s_two_index-1])
                s_one_index = s_one_index - 1
                s_two_index = s_two_index - 1
            elif s_two_index > 0 and scoring_matrix[s_one_index][s_two_index] == horiz_step: # Can we still go left?
                s_one_aligned.append("-")
                s_two_aligned.append(s_two[s_two_index-1])
                s_two_index = s_two_index - 1

            elif s_one_index > 0 and scoring_matrix[s_one_index][s_two_index] == vert_step: # Check if we can travel vertically
                s_two_aligned.append("-")
                s_one_aligned.append(s_one[s_one_index-1])
                s_one_index = s_one_index -1

            # Then check if we have a 

        s_one_aligned.reverse()
        s_two_aligned.reverse()
        s_one_aligned = "".join(s_one_aligned)
        s_two_aligned = "".join(s_two_aligned)
        return scoring_matrix, s_one_aligned, s_two_aligned                



class LocalAlignment:
    mismatch_score: int 
    match_score: int
    gap_score: int
    aligned_sequence_one: str
    aligned_sequence_two: str
    score_matrix = []



    def __init__(self, s_one:str, s_two:str):
        self.mismatch_score = -3
        self.match_score = 3
        self.gap_score = -2

        matrix, as_one, as_two = self.align_sequences(s_one, s_two)
        self.aligned_sequence_one = as_one
        self.aligned_sequence_two = as_two

    
        pass
    
    pass
    def align_sequences(self, s_one, s_two):
        '''
        needleman version of alg. Apparently there is a recursive version of this algorithm that uses less memory. I was not feeling brave enough to do that.
        s_one and s_two are strings to align
        return: a scoring matrix, the first aligned string, the second a lined string as an unpackable in that specific order.
        '''
        s_one_len = len(s_one)
        s_two_len = len(s_two)

        s_one_aligned = []
        s_two_aligned = []

        # Starting score matrix with all zeros everywhere 
        scoring_matrix = [[0.0]*(s_two_len+1) for indices in range(s_one_len +1) ]

        max_score = 0.0
        max_score_loc = [0,0]

        # Walk through the matrix/optimal edge drawing steps
        for s_one_index in range(1, s_one_len+1):

            for s_two_index in range(1, 1+s_two_len):
                diag_step = -math.inf
                

                if s_one[s_one_index-1] == s_two[s_two_index-1]: # When we have a match
                    diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + self.match_score
                else:
                    diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + self.mismatch_score
                
                horiz_step = scoring_matrix[s_one_index][s_two_index-1] + self.gap_score
                vert_step = scoring_matrix[s_one_index-1][s_two_index] + self.gap_score

                scoring_matrix[s_one_index][s_two_index] = max(0.0, horiz_step, diag_step, vert_step) # Include 0 in max score (we can start sub seq from anywhere :))

                if scoring_matrix[s_one_index][s_two_index] > max_score:
                    max_score = scoring_matrix[s_one_index][s_two_index]
                    max_score_loc = [s_one_index, s_two_index]
        


        # Walk back up the graph/matrix starting from the last ele in the matrix
        s_one_index = max_score_loc[0]
        s_two_index = max_score_loc[1]

        while s_one_index > 0 and s_two_index > 0 and scoring_matrix[s_one_index][s_two_index] != 0:
            # Initialize all steps as min cost / worst possible score
            diag_step = -math.inf
            vert_step = -math.inf
            horiz_step = -math.inf
            curr_index_score = scoring_matrix[s_one_index][s_two_index]

            
            # Corner check
            if (s_one_index > 0 and s_two_index > 0): # If we're not touching any of the walls and can still make diags, calc the diag score going up to left
                penalty = 0.0
                if s_one[s_one_index - 1] == s_two[s_two_index-1]:
                    penalty = self.match_score
                else:
                    penalty = self.mismatch_score
                diag_step = scoring_matrix[s_one_index-1][s_two_index-1] + penalty            
            vert_step
            
            if s_one_index > 0: # We can travel up still
                vert_step = scoring_matrix[s_one_index-1][s_two_index] + self.gap_score
            if s_two_index > 0: # We can travel left still
                horiz_step = scoring_matrix[s_one_index][s_two_index-1] + self.gap_score

            

            # Check if we have a match (we can take a diagonal)
            if s_one_index  > 0 and s_two_index> 0 and scoring_matrix[s_one_index][s_two_index] == diag_step:
                s_one_aligned.append(s_one[s_one_index - 1])
                s_two_aligned.append(s_two[s_two_index-1])
                s_one_index = s_one_index - 1
                s_two_index = s_two_index - 1
            elif s_one_index > 0 and curr_index_score == scoring_matrix[s_one_index-1][s_two_index] + self.gap_score:
                # vertical
                s_one_aligned.append(s_one[s_one_index-1])
                s_two_aligned.append("-")
                s_one_index -= 1
            else:
                # left (must have s_two_index > 0)
                s_one_aligned.append("-")
                s_two_aligned.append(s_two[s_two_index-1])
                s_two_index -= 1



        s_one_aligned.reverse()
        s_two_aligned.reverse()
        s_one_aligned = "".join(s_one_aligned)
        s_two_aligned = "".join(s_two_aligned)
        return scoring_matrix, s_one_aligned, s_two_aligned                


# simian_file_names = ["MT-human.fa", "MT-orang.fa"]
# other_file_names = ['q1.fa', 'q2.fa', 't1.fa', 't2.fa']
def gen_unique_pairs(my_list):
    pairs = []
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            pairs.append((my_list[i], my_list[j]))
    return pairs




# print(gen_unique_pairs(other_file_names))

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



def test_global_alignment():
    query_fasta_list = []
    t_fasta_list = []
    with open("data/q1.fa") as query_fasta_file:
        query_fasta_list = get_fasta_as_list(query_fasta_file.read().upper())
    with open("data/t1.fa") as t_fasta_file:
        t_fasta_list = get_fasta_as_list(t_fasta_file.read().upper())
    for i in range(0, len(query_fasta_list)):
        q_fasta = query_fasta_list[i]
        t_fasta = t_fasta_list[i]
        start = dt.now()
        alignment = GlobalAlignment(q_fasta, t_fasta)
        end = dt.now()
        run_time = str(round((end-start).total_seconds()*1000, 2))
        print(f"global-q{i}|python|{run_time}|")    
    
    human_fasta = ""
    orang_fasta = ""
    with open("data/MT-human.fa") as human_fasta_file:
        human_fasta = get_fasta_as_list(human_fasta_file.read().upper())[0]
    with open("data/MT-orang.fa") as tang_fasta_file:
        orang_fasta = get_fasta_as_list(tang_fasta_file.read().upper())[0]
    
    start = dt.now()
    alignment_two = GlobalAlignment(human_fasta, orang_fasta)
    end = dt.now()
    print((end-start).total_seconds()*1000)
    run_time = str(round((end-start).total_seconds()*1000, 2))
    print(f"global-mt_human|python|{run_time}|")


    # for i in range(len(my_list)):
    #     for j in range(i, len(my_list)):
def test_local_alignment():
    query_fasta_list = []
    t_fasta_list = []
    with open("data/q1.fa") as query_fasta_file:
        query_fasta_list = get_fasta_as_list(query_fasta_file.read().upper())
    with open("data/t1.fa") as t_fasta_file:
        t_fasta_list = get_fasta_as_list(t_fasta_file.read().upper())
    for i in range(0, len(query_fasta_list)):
        q_fasta = query_fasta_list[i]
        t_fasta = t_fasta_list[i]
        start = dt.now()
        alignment = LocalAlignment(q_fasta, t_fasta)
        end = dt.now()
        run_time = str(round((end-start).total_seconds()*1000, 2))
        print(f"local-q{i}|python|{run_time}|")    
    human_fasta = ""
    orang_fasta = ""
    with open("data/MT-human.fa") as human_fasta_file:
        human_fasta = get_fasta_as_list(human_fasta_file.read().upper())[0]
    with open("data/MT-orang.fa") as tang_fasta_file:
        orang_fasta = get_fasta_as_list(tang_fasta_file.read().upper())[0]
    start = dt.now()
    alignment_two = LocalAlignment(human_fasta, orang_fasta)
    end = dt.now()
    run_time = str((end-start).total_seconds()*1000)
    print(f"local-mt_human|python|{run_time}|")#(end-start).total_seconds()*1000)


    # for i in range(len(my_list)):
    #     for j in range(i, len(my_list)):



test_global_alignment()
test_local_alignment()

#     pass

