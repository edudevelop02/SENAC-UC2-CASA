'''
=====> em 14-04-2026 <=========
'''
import pandas as pd
import numpy  as np
#=============================
print(f"\nDigite a sua data de nascimento : ")

data_nasc =  int(input("Ano de Nasc. AAAA => "))    # inteiro
idade = 2026 - data_nasc
if  idade >= 18 :
    print(f"  => {idade} Anos é MAIOR de idade  ")
else:
    print(f"  => {idade} Anos é Menor de idade  ")
#
print(f"\nFim")
