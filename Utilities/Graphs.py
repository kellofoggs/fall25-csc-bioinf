from typing import List, Dict, Set, Union, Tuple
from collections import defaultdict
import itertools
import re

'''
This file is used for the various types of graphs used throughout the Rosalind Project problems
Has implementations for edge list graphs, adjacency list graphs etc.
These graphs are helpful in overlap problems and used in Trie/Tree problems 
'''

class DebruijnGraph:
    @staticmethod
    def generate_de_bruijn_graph(k_plus_1_mer_list:List[str], is_adjacency_map:bool=False) -> Union[List[Tuple[str, str]], Dict[str,List[str]] ]:
        '''
        Function that generates a debruijn graph given a list of (k+1)-mers in two formats:
            Adjacency map
            Edge list
        This is set by the optional parameter is_adjacency_map which is a boolean, by default it is set to return
        an edge list. Set to true to return an adjacency map. 
        '''
        k = len(k_plus_1_mer_list[0]) -1 
        
        if not is_adjacency_map:

            debruijn_edges:List[Tuple[str, str]] = []
            for k_plus_1_mer in k_plus_1_mer_list:
                edge_tuple = (k_plus_1_mer[:k], k_plus_1_mer[1:])
                debruijn_edges.append(edge_tuple)
            return(debruijn_edges)
        
        else:
            adjacency_map = defaultdict(list)
            for k_plus_1_mer in k_plus_1_mer_list:
                adjacency_map[k_plus_1_mer[:k]].append( k_plus_1_mer[1:])
            return adjacency_map

class GraphLoader:

    ''' Class used to load graphs from a string format to an object format'''
    
    @staticmethod
    def load_newick_graph_from_string(newick_graph_string: str) ->Union[Dict, List]:
        '''
        Returns a graph as either an adjacency map or edge list, as Newick graphs often have unnamed nodes
        we will use a "DistinctNull" object to differentiate the nodes
        '''
        graph_str_len = len(newick_graph_string)

        left_pointer = 0
        right_pointer = graph_str_len - 1
        opening_bracket_indices:List[int] = []
        closing_bracket_indices:List[int] = []
        bracket_windows:List[Tuple] = []


        for char in newick_graph_string:
            # if len()
            print(char)



        pass

class AdjacencyListNode: 
    '''
    Used for adjacency list graphs
    '''
    children:Set # A set of nodes that are the children of the node
    content:str = None
    
    def __init__(self, content):
        self.content = content
        self.children = set()
        
        pass

    def add_children(self, children: List):
        for child in children:
            self.children.add(child)

    
class Edge:
    # Used for edge list graphs
    source = None
    target = None
    weight: Union[float, int]


        

class Trie:

    '''A class used for tries. This was created for solving
    Introduction to Pattern Mathcing
    The exercise in question just asks for printing out a walk of a trie where the edges
    are symbols in the string and the nodes are states. However I am using this trie to have the nodes be symbols
    This accomplishes the same functionality with a trie as a node cannot have more than one ancestor.
    This means that following the node with symbol x will be the same as jumping to the node with symbol x from the current node



    I chose this method as I think I'll probably have to revisit other trie/graph style problems eventually and
    I personally think edge list is one of the worst ways to represent any sort of graph

       '''
    root_node:AdjacencyListNode = None
    node_order_dict:Dict = None # A dictionary where the key is the object, the value is the order of when it was added into the dict

    '''Make a Trie where each edge node other than the is a '''
    def __init__(self, input_strings):
        self.root_node = AdjacencyListNode(None)
        self.node_order_dict = dict()
        self.node_order_dict[self.root_node] = 1
        self.create_trie_from_strings(input_strings)
        pass

    def create_trie_from_strings(self, input_strings:List[str]):
        for string in input_strings:
            self.add_string_to_graph(string)
            

    def add_string_to_graph(self, string):
        pass
        curr_node = self.root_node
        for char in string:
            child_nodes:Set[AdjacencyListNode] = curr_node.children
            child_is_found = False
            for child in child_nodes:
                # Search child nodes for 
                if child.content == char:
                    curr_node = child
                    child_is_found = True
                    break
            # If we don't find the expected node, then create it
            if not child_is_found:
                new_child = AdjacencyListNode(char)
                curr_node.add_children([new_child])
                curr_node = new_child
                self.node_order_dict[curr_node] = len(self.node_order_dict) + 1

        pass

        
        # 

    def depth_first_print(self):
        # start off at the root node
        
        to_visit_stack = [self.root_node] 
        visited = set()



        while len(to_visit_stack) > 0:
            
            current:AdjacencyListNode = to_visit_stack.pop()
            if current not in visited:
                visited.add(current)
                parent_num = self.node_order_dict[current]

                for child in current.children:
                    child_node_num = self.node_order_dict[child]
                    edge_label = child.content
                    print(f"{parent_num} {child_node_num} {edge_label}")
                    to_visit_stack.append(child)



    def add_node(self, path_to_start:str, ):
        pass

    def add_node(self, parent_node:AdjacencyListNode, child_node_name):
        child_node = AdjacencyListNode(content=child_node_name)
        parent_node.add_children([child_node])

class DNAOverlapGraph:
    '''General Overlap graph, creates edges where source is prefix, target is suffix string and the weight is the maximum overlap between
        Two strings
    '''
    edges: List[Edge]
    overlap_length:int = None
    adjacency_map: Dict[str,List[Tuple]]
    
    # It's better to use a weighted adjacency map here because of constant time hashing
    def __init__(self, word_list:List[str], overlap_length=None):
        self.adjacency_map = defaultdict(list)
        self.overlap_length = overlap_length
        self._construct_overlap_graph(word_list)
        pass

    def _construct_overlap_graph(self, word_list:List[str]):

        # Get all the combinations of words that are not the identity combination i.e. no (AAA, AAA)
        # The first item in the nth tuple is the string whose suffix may match the second tuple elements prefix
        word_combinations = [p for p in itertools.product(word_list, repeat=2) if p[0] != p[1]]

        if self.overlap_length is None:
            '''Construct graph where edges are for max overlap'''
            pass
        elif self.overlap_length > 0:
            # Construct graph where edges are only for overlap of specific length
            pass
        else:
            raise IOError("The overlap length must be either none or greater than 0")
    
    def add_edge(self, source, target, weight):
        edge_tuple = (target, weight)
        self.adjacency_map.get(source).append(edge_tuple)

    
    # def construct_labeled_overlap_graph(sequence_map:Dict[str, str]):
    #     '''Used specifically for DNA sequences, construct an overlap graph where the name of the sequence'''
        # pass

    def strings_do_overlap_by_k(prefix:str, suffix:str, overlap:int):
        prefix_len = len(prefix)
        suffix_len = len(suffix)
        return prefix[prefix_len - overlap:] == suffix[:overlap]
        

class Overlap:
    pass



# class SuffixTrie(Trie):
#     def _
#     pass     
        

    
