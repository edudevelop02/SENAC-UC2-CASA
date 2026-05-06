'''
desenvolva um codigo que: usando IA
faca um programa em python que valide cpf digitado na tela sem uso de import
'''
import pandas as pd
import numpy  as np

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
#dados = 'BaseDPEvolucaoMensalCisp.csv'

df = pd.read_csv(dados, sep=';', encoding='latin1')
print("INICIO ","="*80)
print(df.head())
print("="*80)
print(df.columns)
print("="*80)

def validar_cpf(cpf):
    # Remove qualquer caractere que não seja número manualmente
    cpf_limpo = ""
    for char in cpf:
        if char.isdigit():
            cpf_limpo += char

    # Verifica se tem 11 dígitos ou se todos os números são iguais
    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False

    # Validação dos dois dígitos verificadores
    for i in range(9, 11):
        soma = 0
        for j in range(i):
            soma += int(cpf_limpo[j]) * ((i + 1) - j)
        
        digito = (soma * 10 % 11) % 10
        
        if digito != int(cpf_limpo[i]):
            return False
            
    return True

# Programa principal
entrada = input("Digite o CPF (apenas números ou com pontos/traço): ")

if validar_cpf(entrada):
    print(f"O CPF {entrada} é VÁLIDO.")
else:
    print(f"O CPF {entrada} é INVÁLIDO.")
