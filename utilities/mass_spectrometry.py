from typing import Dict
from math import inf
from decimal import Decimal
class Spectrometry:
    acid_to_spectrometry_string = '''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 
'''
    aa_mm_pairs = list(map(lambda x: (x.split()[0], round(float(x.split()[1]), 4)), acid_to_spectrometry_string.splitlines()))
    _amino_acid_to_monoisotopic_mass:Dict = dict(aa_mm_pairs)
    _mm__aa_pairs = sorted([(mass, amino_acid) for amino_acid, mass in aa_mm_pairs], key=lambda x: x[0])
    # print(_mm__aa_pairs)
    _mono_isotope_mass_to_amino_acid:Dict = dict(_mm__aa_pairs)

    @staticmethod
    def get_mass_from_amino_acid(amino_acid)->float:
        return Spectrometry._amino_acid_to_monoisotopic_mass.get(amino_acid)
    
    @staticmethod
    def get_amino_acid_from_mass(mono_isotopic_mass:float)->str:
        '''
        Original:
            Return the amino acid with the closest mass to what is given using linear search as there aren't that many values in our table
            This avoids having to round and rounding errors

        New: 
            It seems like the good folks at rosalind assume that there are no tie breakers/we round the masses to the 4th decimal place I'll just use the dictionary
            This solution is poor as it only works when there is an exact match between the float in the key of the dict and whats passed into this function
            Floats are remarkable inconsistent so I really wish a different method was used. Because all of the masses are near the floar of the nearest integer we could also 
            just floor all values in the table, but then we'd have to round all the inputs to the nearest whole number
        '''
                # print(Spectrometry._mono_isotope_mass_to_amino_acid)
        acid =  Spectrometry._mono_isotope_mass_to_amino_acid.get(round(mono_isotopic_mass, 4))
        if acid is None: print(f"None mass: {mono_isotopic_mass}")
        return acid
        


    
