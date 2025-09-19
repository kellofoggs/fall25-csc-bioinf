from code.codon_src.file_tools import Fasta
import os
import subprocess
import zipfile
import glob
from datetime import datetime as dt

base_dir_path = os.path.dirname(__file__)
week_data_dir = os.path.join(base_dir_path, "data")

print(base_dir_path)
# python_contigs = Fasta.get_fasta_as_list()
# codon_contigs = Fasta.get_fasta_as_list()

# First compile the binary version using codon
codon_binary_cmd_template = "./main_codon {data_dir_path}"
# subprocess.run() # Shell opens in the current working directory where interpreter was started

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

def main():
    # Firstly compile the binary for codon to avoid having to use codon run
    source_code_dir_path = os.path.join(base_dir_path, "code")
    run_setup(source_code_dir_path)
    data_directories = ["data1","data2","data3","data4"]
    # data_directories = ["data4"]

    results_list = []
    output_table = [["Dataset", "Language","Runtime","N50"]]

    for directory in data_directories:
        data_dir_path = os.path.join(week_data_dir, directory)
        start = dt.now()
        python_n50 = python_run(data_dir_path)
        end = dt.now()
        python_result = [directory, "python", str(end-start).split('.')[0], python_n50]

        start = dt.now()
        codon_n50 = codon_run(data_dir_path)     
        end = dt.now()
        codon_result = [directory, "codon", str(end-start).split('.')[0], codon_n50]
        output_table.append(python_result)
        output_table.append(codon_result)

    # for element in results_list:
    #     output_table.append([element["dataset" ], element['language'], element["runtime"], element['N50']])
    index = 0
    for row in output_table:
        print("{:<15} {:<15} {:<15} {:<15}".format(*row))
        if index == 0:
            print("----------------------------------------------------------------")
            index = index + 1
    return results_list
    # subprocess.run(f"pwd && cd {week_data_dir} && {[]}")



def get_contig_lengths(data_dir_path):
    with open(os.path.join(base_dir_path,f"{data_dir_path}/contig.fasta")) as contig_file:
        contigs = Fasta.get_fasta_as_list(contig_file.read())
        return list(map(len, contigs))
    
def python_run(data_dir_path: str):
    # subprocess.run(f"pwd && cd {base_dir_path} && ulimit -s 8192000 && python code/pysrc/main.py {data_dir_path} > /dev/null",shell=True)  
    subprocess.run(f"pwd && cd {base_dir_path} && ulimit -s 8192000 && python code/pysrc/main.py {data_dir_path}",check==True,shell=True)  

    n_50 = calculate_N50(get_contig_lengths(data_dir_path))
    return n_50

def codon_run(data_dir_path: str):
    subprocess.run(f"pwd && cd {base_dir_path} && ulimit -s 8192000 && ./main_codon {data_dir_path}",shell=True, check=True)
    n_50 = calculate_N50(get_contig_lengths(data_dir_path))
    return n_50


def run_setup(source_code_dir_path):
    '''
    Unzip files and compile source code using codon and release flag
    '''
    codon_compile_cmd = "/.codon build -release code/codon_src/main.codon -o main_codon"
    try:
        result = subprocess.run(f'pwd && cd {base_dir_path} && {codon_compile_cmd}', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(base_dir_path)
        print(codon_compile_cmd)
        print(e.stdout)
        print(e.stderr)
    data_zip_glob = "data*.zip"
    for zip_path in glob.glob(os.path.join(week_data_dir, data_zip_glob)):
        os.makedirs(week_data_dir, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(week_data_dir)



main()

 #TODO: Use codon bridge to run some utilities with the python interpreter 