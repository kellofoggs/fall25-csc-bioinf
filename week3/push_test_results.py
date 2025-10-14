with open("test/python_tests_out") as py_results_file:
    python_test_results = [line.strip().split() for line in py_results_file]

with open("test/codon_tests_out") as codon_results_file:
    codon_test_results = [line.strip().split() for line in codon_results_file]

print(f"{'Language':<10} {'Test Name':<25} {'Test Result':<10}")
print("-" * 50)

for py, cod in zip(python_test_results, codon_test_results):
    print(f"{'python':<10} {py[0]:<25} {py[1]:<10}")
    print(f"{'codon':<10} {cod[0]:<25} {cod[1]:<10}")
