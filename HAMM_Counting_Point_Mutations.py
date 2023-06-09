# -*- coding: utf-8 -*-
"""HAMM: Counting Point Mutations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19nkXuXrixLksxX2f8YcdXbryxzVHt1i4

## HAMM: [Counting Point Mutations](https://rosalind.info/problems/hamm/)
"""

def hamm(input_string):
  """Solve https://rosalind.info/problems/hamm/

  Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
  Return: The Hamming distance dH(s,t). """

  s, t = input_string.splitlines()

  if len(s) == len(t):
    dH = 0
    for i in range(len(s)):
      if s[i] != t[i]:
        dH += 1
    return str(dH)
  else:
    return "Strings must be the same length"

sample_data= 'GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT'
hamm(sample_data) == '7'

from google.colab import files

def string_from_uploaded_file():  
  uploaded = files.upload() # https://colab.research.google.com/notebooks/io.ipynb#scrollTo=BaCkyg5CV5jF
  for bytesObject in uploaded.values(): # https://www.w3schools.com/python/ref_dictionary_values.asp
    return bytesObject.decode('utf-8') # https://pythonexamples.org/python-bytes-to-string/#3
    
input_string = string_from_uploaded_file()
output_string = hamm(input_string)
print(output_string)
with open('rosalind_hamm_output.txt', 'w') as f:
  f.write(output_string)
files.download('rosalind_hamm_output.txt') # https://colab.research.google.com/notebooks/io.ipynb#scrollTo=hauvGV4hV-Mh