# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.
from datetime import datetime as dt
start = dt.now()
from os.path import join
import numpy as np
import biotite.sequence.phylo as phylo
# from tests.util import data_dir


# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.




# import biotite.sequence.phylo as phylo
# from .util import data_dir

# @python
# def RunTests(): # This is some of that python magic/nonsense, we're declaring a Unittest class in a function
    
    
    # pass

distances: np.ndarray[int,2] = np.loadtxt("distances.txt", dtype=np.int64)
tree = phylo.upgma(distances)
upgma_newick:str = ""

with open("newick_upgma.txt", "r") as file:
    upgma_newick = file.read().strip()

def test_distances(tree):
    # Tree is created via UPGMA
    # -> The distances to root should be equal for all leaf nodes
    # print(tree.to_newick(include_distance=False))
    # print(tree)
    try:

        dist = tree.root.distance_to(tree.leaves[0])
        for leaf in tree.leaves:
            assert leaf.distance_to(tree.root) == dist
        assert tree.get_distance(0, 19, True) == 9
        assert tree.get_distance(4, 2, True) == 10
        return "test_distances passed"
    except AssertionError as e:
        return "test_distances failed"

def test_upgma(tree, upgma_newick):
    """
    Compare the results of `upgma()` with DendroUPGMA.
    """
    try:
        ref_tree = phylo.Tree.from_newick(upgma_newick)
        # Cannot apply direct tree equality assertion because the distance
        # might not be exactly equal due to floating point rounding errors
        for i in range(len(tree)):
            for j in range(len(tree)):
                # Check for equal distances and equal topologies
                assert abs(tree.get_distance(i, j) - ref_tree.get_distance(i, j)) <= 1e-3

                assert tree.get_distance(i, j, topological=True) == ref_tree.get_distance(
                    i, j, topological=True
                )
        return "test_upgma passed"
    except AssertionError as e:
        return "test_distances failed"
def test_neighbor_joining():
    """
    Compare the results of `neighbor_join()` with a known tree.
    """
    try:

        dist = np.array([
            [ 0,  5,  4,  7,  6,  8],
            [ 5,  0,  7, 10,  9, 11],
            [ 4,  7,  0,  7,  6,  8],
            [ 7, 10,  7,  0,  5,  9],
            [ 6,  9,  6,  5,  0,  8],
            [ 8, 11,  8,  9,  8,  0],
        ])  # fmt: skip

        ref_tree = phylo.Tree(
            phylo.TreeNode(
                [
                    phylo.TreeNode(
                        [
                            phylo.TreeNode(
                                [
                                    phylo.TreeNode(index=0),
                                    phylo.TreeNode(index=1),
                                ],
                                [1, 4],
                            ),
                            phylo.TreeNode(index=2),
                        ],
                        [1, 2],
                    ),
                    phylo.TreeNode(
                        [
                            phylo.TreeNode(index=3),
                            phylo.TreeNode(index=4),
                        ],
                        [3, 2],
                    ),
                    phylo.TreeNode(index=5),
                ],
                [1, 1, 5],
            )
        )

        test_tree = phylo.neighbor_joining(dist)

        assert test_tree == ref_tree
        return "test_neighbor_joining passed"
    except AssertionError as e:
        return "test_neighbor_joining failed"






results = []
results.append(test_distances(tree))
results.append(test_upgma(tree, upgma_newick))
results.append(test_neighbor_joining())
end = dt.now()
print((end-start).total_seconds()*1000)

with open("python_tests_out", 'w') as file:
    for i in range(0, len(results)):
        result = results[i]
        file.write(result)
        if i +1 < len(results):
            file.write("\n")

