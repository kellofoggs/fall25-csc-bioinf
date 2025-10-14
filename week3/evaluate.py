# from utilities.file_tools import Fasta
import os
import subprocess
import zipfile
import glob
from datetime import datetime as dt
from typing import List


base_dir_path = os.path.dirname(__file__)
week_data_dir = os.path.join(base_dir_path, 'data')


# First compile the binary version using codon
codon_binary_cmd_template = './test_codon'

def calculate_N50(contig_len_list:list[int]) -> int:
    total_len = sum(contig_len_list)
    contig_len_list.sort(reverse=True)
    
    half_len = total_len/2
    cur_len = 0
    index = 0
    for length in contig_len_list:
        
        cur_len += length
        if cur_len >= half_len:
            return length

def create_contigs(data_dir:str):

    # Create the contigs using the python interpreter
    codon_run(data_dir)
    python_run(data_dir)

    pass

def read_fasta(fasta_file:List[str]):
    data = []
    for line in fasta_file:
        line = line.strip()
        if line[0] != '>':
            data.append(line)
    # print(name, len(data), len(data[0]))
    # print('Sample:', data[0])
    return data


def main():
    # Firstly compile the binary for codon to avoid having to use codon run
    source_code_dir_path = os.path.join(base_dir_path, 'code')
    # run_setup(source_code_dir_path)
    codon_test_output = codon_run()
    python_test_output = python_run()
    print(f"{'Language':<10} {'Runtime':>10}")
    print("-" * 21)
    print(f"{'python':<10} {python_test_output.strip():>6}ms")
    print(f"{'codon':<10} {codon_test_output.strip():>6}ms")




    




def get_contig_lengths(data_dir_path):
    with open(os.path.join(base_dir_path,f'{data_dir_path}/contig.fasta')) as contig_file:
        contigs = read_fasta(contig_file.readlines())
        return list(map(len, contigs))
    
def python_run():
    result = subprocess.run(f'cd test  && ulimit -s 8192000 && python test_phylo.py', capture_output=True, cwd= base_dir_path, check=True,shell=True, text=True)  
    return(str(result.stdout))
    # n_50 = calculate_N50(get_contig_lengths())
    # return n_50

def codon_run():
    # print(base_dir_path)
    subprocess.run(f'cd test && codon build -release test_phylo.codon -o test_phylo',cwd= base_dir_path, shell=True, check=True)

    result = subprocess.run(f'cd test && ./test_phylo',cwd= base_dir_path, shell=True, check=True, capture_output=True, text=True)
    return str(result.stdout)

    


def run_setup(source_code_dir_path):
    '''
    Unzip files and compile source code using codon and release flag
    '''
    # codon_compile_cmd = '~/.codon/bin/codon build -release code/codon_src/main.codon -o main_codon'
    codon_compile_cmd = 'codon build -release code/codon_src/main.codon -o main_codon'

    # try:
    result = subprocess.run(f'pwd && {codon_compile_cmd}',  shell=True, check=True, cwd= base_dir_path, capture_output=True)
    # except subprocess.CalledProcessError as e:
    #     print(base_dir_path)
    #     print(codon_compile_cmd)
    #     print(e.stdout)
    #     print(e.stderr)

    data_zip_glob = 'data*.zip'
    for zip_path in glob.glob(os.path.join(week_data_dir, data_zip_glob)):
        os.makedirs(week_data_dir, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(week_data_dir)



main()

 #TODO: Use codon bridge to run some utilities with the python interpreter 