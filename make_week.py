arguments_description = '''Author: Kelly Ojukwu

This is a simple utility script that creates a directory for a weekly assignment. 
Each weekly assignment is contained in a directory with the following structure:
This file should be left in the root directory of the github repo and should not be moved as it uses
the python __file__ special attribute
week1/     <- Week 1 deliverable
   code/   <- source code
   data/   <- data files
   test/   <- tests
   ai.txt  <- prompt information and AI tool identification

The argument here should be the number/name of the week i.e. 
'''

import argparse
import os

abs_file_path = os.path.abspath(__file__)
root_dir_path = os.path.dirname(abs_file_path)
subdir_names = ["code", "data", "test"]
file_names = ["ai.md"]

print(abs_file_path)

def create_assignment_directory(week_name):
    
   week_dir_name = os.path.join(root_dir_path, f"week{week_name}")
    
   os.makedirs(week_dir_name,exist_ok=True)
   for sub_dir in subdir_names:
      sub_dir_path = os.path.join(week_dir_name,sub_dir)
      os.makedirs(sub_dir_path,exist_ok=True)

   for file_name in file_names:
      with open(os.path.join(week_dir_name, file_name), 'a'):
         pass

arguments_description = '''This 
'''
parser = argparse.ArgumentParser(description=arguments_description)
parser.add_argument("week_name", nargs="?", help="The number/name of the week that the assignment is for")
args = parser.parse_args()
create_assignment_directory(week_name=args.week_name)
