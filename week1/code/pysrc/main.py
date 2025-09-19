from dbg import DBG
from utils import read_data
import sys
import os
from datetime import datetime as dt

sys.setrecursionlimit(1000000)


if __name__ == "__main__":

    argv = sys.argv
    start = dt.now()
    short1, short2, long1 = read_data(os.path.join('./', argv[1]))

    k = 25
    dbg = DBG(k=k, data_list=[short1, short2, long1])
    # dbg.show_count_distribution()
    with open(os.path.join('./', argv[1], 'contig.fasta'), 'w') as f:
        for i in range(20):
            c = dbg.get_longest_contig()
            if c is None:
                break
            print(i, len(c))
            f.write('>contig_%d\n' % i)
            f.write(c + '\n')
    end = dt.now()
    print(end-start)