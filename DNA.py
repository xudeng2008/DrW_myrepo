#!/usr/bin/python3
s = open('rosalind_dna.txt','r').read()
for n in ["A","C","G","T"]:
    print(s.count(n), end=' ')
print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))
