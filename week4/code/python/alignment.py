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

