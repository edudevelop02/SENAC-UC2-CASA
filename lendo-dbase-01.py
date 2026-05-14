# %% [markdown]
# lendo arquivos dbase.dbf e convertendo para .csv

# %%
#%pip install dbfread
import sys
print(sys.executable)


# %%
import dbfread
print(f"Versão instalada: {dbfread.__version__}")  


# %%
#%pip install duckdb
import duckdb



# %%
import pandas as pd
from dbfread import DBF    
# instalar pelo terminal a biblioteca : pip install dbfread 
# Summary: Read DBF Files with Python
# Home-page: https://dbfread.readthedocs.io/

import numpy as np 
import os

DbasePath = r'C:\@PROGRAMACAO_01\SENAC-UC2-CASA\dados'
DbaseFile = 'PRO00.DBF'

# Concatenando com f-string
# Adicionamos uma barra entre elas se o Path já não terminar com uma
caminho_completo = fr'{DbasePath}\{DbaseFile}'

print("Caminho do arquivo: ",caminho_completo)


# %%
import os
#DbasePath = r'C:\@PROGRAMACAO_01\SENAC-UC2-CASA\dados'
DbasePath = r'dados'
DbaseFile = 'PRO00.DBF'
caminho_completo2 = os.path.join(DbasePath, DbaseFile)
print(f"Caminho do arquivo os: ({caminho_completo2})  ")


# %%
#import duckdb
print(f'Fazendo conexao com DuckDB ...  {caminho_completo2} ')
# 1. Conecta (ou usa a conexão padrão)
con = duckdb.connect()

# 2. Instala e carrega a extensão necessária para ler DBF
#con.execute("INSTALL spatial;")
#con.execute("LOAD spatial;")

# Cria uma conexão explícita com o banco em memória
con = duckdb.connect(database=':memory:')

# Tenta carregar. Se falhar, instala e carrega.
try:
    con.execute("LOAD spatial;")
    print("Carregando extensao spatial ... ")
except:
    print("Extensão não encontrada. Instalando spatial...")
    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")

print("DuckDB pronto para uso!")

# 3. Agora sua consulta vai funcionar
#caminho_completo2 = r'C:\@PROGRAMACAO_01\SENAC-UC2-CASA\dados\PRO00.DBF'

# 2. Prepara a busca: remove espaços do codigo_entrada do usuário
codigo_entrada = '587'
codigo_busca_10 = codigo_entrada.strip().rjust(10)   # fica so com os dados, sem espaços e com tamanho de 10 bytes
codigo_busca = codigo_entrada

# Use a conexão 'con' para fazer a query
query = f"SELECT * FROM st_read('{caminho_completo2}') WHERE TRIM(PRO_CODIGO) = '{codigo_busca}'"
#query = f"SELECT * FROM st_read('{caminho_completo2}') WHERE (PRO_CODIGO) = '{codigo_busca}'"   # NAO FUNCIONA
print(query)

registro = con.execute(query).df()

if not registro.empty:
    codigo = registro['PRO_CODIGO'].iloc[0]
    descricao = registro['PRO_DESC'].iloc[0]
    pr_venda = registro['PRO_PVENDA'].iloc[0]
    # Formata primeiro com o ponto e duas casas decimais
    pr_venda_formatado = f"{pr_venda:.2f}"
    # Substitui o ponto pela vírgula para o padrão brasileiro
    pr_venda_final = pr_venda_formatado.replace('.', ',')
    print(f"Codigo Produto: ({codigo_busca_10}) | Descricao: {descricao} | Preco de Venda: {pr_venda_final}")
    print(f"Codigo Produto: ({codigo}) | Descricao: {descricao} | Preco de Venda: {pr_venda_final}")
    print(registro)
else:
    print("Produto não encontrado.")


# %%
# Comando SQL para buscar o Codigo 104
# Note que usamos rjust(10) dentro do SQL se o dado ainda estiver com espaços
query = f"""
    SELECT PRO_DESC, PRO_PVENDA 
    FROM st_read('{caminho_completo2}') 
    WHERE TRIM(PRO_CODIGO) = '104'
"""

# Executa e transforma em um DataFrame ou lista
print(f'Fazendo query com DuckDB ...>>>  {caminho_completo2} ')
resultado = con.execute(query).df()
#resultado = duckdb.query(query).to_df()

if not resultado.empty:
    print(f"Descricao: {resultado['PRO_DESC'].iloc[0]}")
    print(f"Preco: {resultado['PRO_PVENDA'].iloc[0]}")
else:
    print("Produto não encontrado.")


# %%
try:
    # O parametro ignore_missing_memofile=True ajuda se o .DBF tiver campos Memo (.DBT) faltando
#    tabela = DBF(caminho_completo, ignore_missing_memofile=True)
# Use o 'with' para garantir que o arquivo seja liberado após a leitura
    with DBF(caminho_completo2, ignore_missing_memofile=True) as tabela:
        df = pd.DataFrame(tabela)

    print("Sucesso! O arquivo tem", len(df), "registros.")
    print(df.head()) 
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# %%
DbasePath = r'C:\@PROGRAMACAO_01\SENAC-UC2-CASA\dados'
DbaseFile = 'PRO00.DBF'

# Concatenando com f-string
# Adicionamos uma barra entre elas se o Path já não terminar com uma
caminho_completo = fr'{DbasePath}\{DbaseFile}'
print(DbasePath)
print(DbaseFile)
print(caminho_completo)


# %%
print('=============================================')
# Testando a leitura
try:
    # O parametro ignore_missing_memofile=True ajuda se o .DBF tiver campos Memo (.DBT) faltando
#    tabela = DBF(caminho_completo, ignore_missing_memofile=True)
# Use o 'with' para garantir que o arquivo seja liberado após a leitura
    with DBF(caminho_completo, ignore_missing_memofile=True) as tabela:
        df = pd.DataFrame(tabela)

    print("Sucesso! O arquivo tem", len(df), "registros.")
    print(df.head()) 
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# %% [markdown]
# # 1. Primeiro, vamos ver EXATAMENTE como o dado está no seu DataFrame
# exemplo_real = df['PRO_CODIGO'].iloc[0]
# print(f"DEBUG - Valor original no arquivo: '{exemplo_real}'")
# print(f"DEBUG - Tipo do dado: {type(exemplo_real)}")
# x = input("   TECLE ENTER ===> ")   

# %%
# Definindo o Codigo que você quer buscar

print(f"\nDigite o codigo do produto para listar. ")
codigo_entrada = input("   Codigo do Produto ===> ")   # inteiro
# 2. Prepara a busca: remove espaços do codigo_entrada do usuário
codigo_busca = codigo_entrada.strip().rjust(10)   # fica so com os dados, sem espaços e com tamanho de 10 bytes
print(f'Buscar codigo:({codigo_busca})')
print(f'               ---------- ')

# Filtrando o DataFrame
# Certifique-se de que o nome da coluna é exatamente PRO_CODIGO
registro = df.loc[df['PRO_CODIGO'] == codigo_busca]    # busca o codigo na coluna PRO_CODIGO e retorna o registro correspondente

if not registro.empty:
    # Acessando o valor da coluna PRO_DESC  PRO_PVENDA .iloc[0]
    codigo = registro['PRO_CODIGO'].iloc[0]
    descricao = registro['PRO_DESC'].iloc[0]
    pr_venda = registro['PRO_PVENDA'].iloc[0]
    # Formata primeiro com o ponto e duas casas decimais
    pr_venda_formatado = f"{pr_venda:.2f}"
    # Substitui o ponto pela vírgula para o padrão brasileiro
    pr_venda_final = pr_venda_formatado.replace('.', ',')
    print(f"Codigo Produto: ({codigo}) | Descricao: {descricao} | Preco de Venda: {pr_venda_final}")
else:
    print(f"Registro com Codigo {codigo_busca} NÂO encontrado.")

# %%
print('\n================  FIM  =============================')
#url = 'pedidos_narashop.csv'
#df = pd.read_csv(url, encoding='utf8', sep=';')
#df.head()


