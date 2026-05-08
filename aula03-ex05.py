'''

'''
print(f"\nDigite a sua Data de nascimento e Genero  : ")

data_atu =  (input("Data Atual   => "))
if data_atu == "" :
    data_atu = 2026
data_atu =  int(data_atu)    
print(f"Data Atual: {data_atu} ")

data_nasc =  (input("Data Nascimento      => "))
data_nasc =  int(data_nasc)    # converte p inteiro
genero =        (input("Genero 'M' ou 'F' => "))    # string
idade = 2026 - data_nasc
if  idade >= 18 and genero == "M" or genero == "m" :
    print(f"  => {idade} Anos Esta apto para a se alistar  ")
else:
    print(f"  => Idade: {idade} Anos e Genero: {genero} NAO Esta apto para a se alistar  ")
#
print(f"\nFim")
