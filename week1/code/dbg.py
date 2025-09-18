from dna import DNAStringTools

class DeBruijnNode[E]:
    # A Node that holds a k-mer and other fields useful for building a DeBruijn Graph

    _adjacent_nodes: set[Optional[DeBruijnNode[E]]] # type: ignore # A list of nodes that this node has an edge going towards
    content : E
    _num_nodes: int # How often this node that represents a k_mer appears each time
    max_depth_child: Optional[DeBruijnNode[E]] # type: ignore
    path_depth: int

    def __init__(self, content:E):
        self.content = content
        self._adjacent_nodes = set()
        self._num_nodes = 0 # How many times this node appears in the graph
    
    def reset_path_data(self):
        self.max_depth_child = None
        self.path_depth = 0

    @property
    def children(self) -> list[Optional[DeBruijnNode[E]]]: # type: ignore
        adjacent_nodes: set = self._adjacent_nodes
        return list(adjacent_nodes)
    @property
    def sorted_children(self) -> list[Optional[DeBruijnNode[E]]]: # type: ignore
        return sorted(self.children, key= lambda child_node: child_node.num_nodes, reverse=True)

    @property
    def num_nodes(self) -> int:
        return self._num_nodes

    def add_kmer(self) -> None: 
        '''
        Increment the count of how many times this kmer appears in the graph
        '''
        self._num_nodes += 1

    def add_child(self, child_node: Optional[DeBruijnNode[E]]): # type: ignore
        self._adjacent_nodes.add(child_node) # Use a set to avoid duplicate edges

    
    def __eq__(self, other: DeBruijnNode ) -> bool: # type: ignore
        if not isinstance(other, DeBruijnNode):
            return False
        else:
            return self.content == other.content
        
    def __ne__(self, other: DeBruijnNode ) -> bool: # type: ignore
        '''
        Explicitly required as it looks like codon does not automatically infer this from __eq__
        '''
        return not self.__eq__(other)
    
    def remove_children(self, children_to_remove:set[Optional[DeBruijnNode[E]]]): # type: ignore
        self._adjacent_nodes = self._adjacent_nodes - children_to_remove
    
    def __hash__(self):
        return hash(self.content) 
    
    def __str__(self):
        return f"{self.content}"

    def __repr__(self):
        return self.__str__()[-1]



class DebruijnGraph:

    '''
    A DeBruijn Graph for the implementation of Hamiltonian Path  using adjacency list representation.
    This graph contains nodes for each kmer and their reverse complements.

    '''
    k : int
    kmer_to_node_dict: dict[str, DeBruijnNode[str]]
    node_id_to_node: dict[int, DeBruijnNode[str]]
    path: list[DeBruijnNode[str]]
    visited_set: set[DeBruijnNode[str]]

    def __init__(self, reads: list[str], k:int):
        self.visited_set: set[DeBruijnNode[str]] = set()
        self.kmer_to_node_dict = {}
        self._generate_de_bruijn_graph(reads, k)

    def print_dbg(self):
        kmer_nodes = sorted([node for node in self.kmer_to_node_dict.values()], key= lambda x: ( x.num_nodes, x.content))
        for node in kmer_nodes:
            print(f"{node.content} ({node.num_nodes}) -> {sorted([child.content for child in node.children])}")

    
    
    def _generate_de_bruijn_graph(self, reads: list[str], k:int) -> None:
        '''
        Function that generates a DeBruijn graph from a list of reads and a kmer length k.
        This graph includes both the kmers from the reads and their reverse complements.
        Args:
            reads (list[str]): A list of DNA strings (reads) to generate the DeBruijn graph from
            k (int): The length of the kmers to generate from the reads
        Returns:
            None: The graph is stored in the instance variable kmer_to_node_dict
        '''
        for read in reads:
            self._add_read_kmers_to_graph(read, k)
            self._add_read_kmers_to_graph(DNAStringTools.reverse_complement_dna(read), k)

    def _add_read_kmers_to_graph(self, read: str, k:int) -> None:
        '''
        Adds all but the last kmers from a read to the DeBruijn graph
        Args:
            read (str): The DNA string (read) to generate the kmers from
            k (int): The length of the kmers to generate from the read
        Returns:
            None: The graph is stored in the instance variable kmer_to_node_dict
        '''
        prev_kmer = None
        # In the original Python implementation the last kmer is erroneously omitted from the result,
        # This behavior is replicated here for consistency with the original implementation. 
        # Unfortunately for us that means that I will not be using a generator here as I need to look ahead one kmer, this would required me to either rewrite the generator function or write a wrapper for it
        # I have opted to consume the generator into a list instead
        # for curr_kmer in DNAStringTools.generate_kmers(read, k): # My original implementation that includes the last kmer, which is the correct behavior

        for curr_kmer in list(DNAStringTools.generate_kmers(read, k))[:-1]:
            if prev_kmer is None:
                prev_kmer = curr_kmer
                continue
            self._add_arc(prev_kmer,curr_kmer)

            prev_kmer = curr_kmer


    def _add_arc(self, kmer_from:str, kmer_to:str):
        '''
        Adds a directed edge from kmer_from to kmer_to in the DeBruijn graph.
        If the nodes for the kmers do not exist, they are created.
        Args:
            kmer_from (str): The kmer that the edge is directed from
            kmer_to (str): The kmer that the edge is directed to
        '''
        node_one = self._add_node(kmer_from)
        node_two = self._add_node(kmer_to)
        node_one.add_child(node_two) # Use object reference instead of idx used by Zhongyu Chen

    def _add_node(self, kmer:str) -> DeBruijnNode[str]:
        '''
        Adds a new node to the DeBruijn graph if it doesn't already exist, returns the node's object reference.
        Args:
            kmer (str): The kmer that the node represents
        Returns:
            DeBruijnNode[str]: The node object reference for the kmer
        '''       

        if kmer not in self.kmer_to_node_dict:
            # Create a new node object if it doesn't exist
            # node = DeBruijnNode(kmer)  # In the original implementation the number of nodes was tracked with a value incremented on each Node creation
            # This value was neither decremented or used even if nodes were removed, so I don't see the point of it
            self.kmer_to_node_dict[kmer] = DeBruijnNode(kmer) # We can get the same functionality here using len of dict as this is constant time operation in python
        node = self.kmer_to_node_dict[kmer]
        node.add_kmer()
        return node



    # Contig construction methods    
    def get_longest_contig(self):
        self.visited_set: set[DeBruijnNode[str]] = set()
        for node in self.kmer_to_node_dict.values():
            # Reset the max path depth for all nodes
            node.reset_path_data()
        longest_path = self._construct_globally_longest_path()

        # Concatenate kmers so that they form a contig
        output = str(longest_path[0]) + "".join(list(map(lambda x: x.__str__()[-1], longest_path[1:])))
        self.delete_path(longest_path)

        return output

    def _construct_globally_longest_path(self) -> list[Optional[DeBruijnNode[str]]]: # type: ignore
        max_depth = 0
        deepest_node: Optional[DeBruijnNode[str]] = None # type: ignore
        for node_key in self.kmer_to_node_dict.keys():
            node = self.kmer_to_node_dict[node_key]
            depth:int  = self._get_path_depth_recur(node)
            if depth > max_depth:
                max_depth = depth
                deepest_node = node
            
        path = []
        while deepest_node is not None:
            path.append(deepest_node)
            deepest_node = deepest_node.max_depth_child
        return path
              
    def _get_path_depth_recur(self, start_node: Optional[DeBruijnNode[str]]) -> int:   # type: ignore
        max_depth = 0
        max_child: Optional[DeBruijnNode[str]] = None # type: ignore

        if not start_node  in self.visited_set:
            self.visited_set.add(start_node)
            for child in start_node.sorted_children:
                depth = self._get_path_depth_recur(child) # Go down each path recursively
                # Come back up comparing path length to other path lengths at latest branch
                # Keep the deepest branch path
                if depth > max_depth:
                    max_child = child
                    max_depth = depth
            start_node.path_depth = max_depth + 1


            pass
            start_node.max_depth_child = max_child
        return start_node.path_depth  # max_depth_child
    
    def delete_path(self, path: list[Optional[DeBruijnNode[str]]]): # type: ignore
        for node in path:
            del self.kmer_to_node_dict[node.content]
        path_set:set[Optional[DeBruijnNode[str]]] = set(path) # type: ignore
        for node in self.kmer_to_node_dict.values():
            node.remove_children(path_set)




    # Old method for solving a problem on Rosalind.INFO that required generating a DeBruijn graph from a list of (k+1)-mers
    # @staticmethod
    # def generate_de_bruijn_graph(k_plus_1_mer_list:list[str], is_adjacency_map:bool=False) -> Union[list[tuple[str, str]], dict[str,list[str]] ]:
    #     '''
    #     Function that generates a debruijn graph given a list of (k+1)-mers in two formats:
    #         Adjacency map
    #         Edge list
    #     This is set by the optional parameter is_adjacency_map which is a boolean, by default it is set to return
    #     an edge list. Set to true to return an adjacency map. 
    #     '''
    #     k = len(k_plus_1_mer_list[0]) -1 
        
    #     if not is_adjacency_map:

    #         debruijn_edges:list[tuple[str, str]] = []
    #         for k_plus_1_mer in k_plus_1_mer_list:
    #             edge_tuple = (k_plus_1_mer[:k], k_plus_1_mer[1:])
    #             debruijn_edges.append(edge_tuple)
    #         return debruijn_edges
        
    #     else:
    #         adjacency_map = defaultdict(list)
    #         for k_plus_1_mer in k_plus_1_mer_list:
    #             adjacency_map[k_plus_1_mer[:k]].append( k_plus_1_mer[1:])
    #         return adjacency_map

