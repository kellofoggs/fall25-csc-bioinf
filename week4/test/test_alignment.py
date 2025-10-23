import re
from datetime import datetime as dt
start = dt.now()

from .alignment import GlobalAlignment, LocalAlignment
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

