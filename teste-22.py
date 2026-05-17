# %%
'''
listar dados lendo uma base de dados externa
em 15-05-2026

'''
import pandas as pd
import numpy  as np

#dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
dados = 'BaseDPEvolucaoMensalCisp.csv'

df = pd.read_csv(dados, sep=';', encoding='latin1')
print(df)

# %%
# mOSTRA O NOME DAS COLUNAS DE DADOS
print(df.columns)

# %%
print(df.shape)

# %%
print(df.dtypes)   # exibe tipos de dados

# %%
print(df.describe())

# %%
# Agrupando por CISP e somando os furtos de celular
df_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()
# Ordenando do maior para o menor
df_cisp = df_cisp.sort_values(by='furto_celular', ascending=False)
print(df.cisp) 

# %%
print(df.info() )   # estatisticas das colunas de dados

# %%
#filtros usando .loc
# Usando .loc
df_capital = df.loc[df['munic'] == 'Rio de Janeiro']
# Usando .query() — sintaxe alternativa mais legível
df_capital = df.query("munic == 'Rio de Janeiro'")
# Repetindo o groupby apenas para a capital
df_cisp_capital = df_capital.groupby('cisp')['furto_celular'].sum().reset_index()
df_cisp_capital = df_cisp_capital.sort_values(by='furto_celular', ascending=False)
print(f'Estatisticas Na Capital para: {df_cisp_capital}')

# %%
# df_cisp_capital já foi criado no passo anterior (groupby + reset_index)
array_furto = np.array(df_cisp_capital['furto_celular'])
array_furto


# %%
# Minimo, maximo, Média e Mediana
maximo = np.max(array_furto)
minimo = np.min(array_furto)
media  = np.mean(array_furto)
mediana = np.median(array_furto)
print(f'O valor maximo  é {maximo}')
print(f'O valor minimo  é {minimo}')
print(f'O valor medioo  é {media}')
print(f'O valor mediano é {mediana}')



# %%
# Quartis: Linhas de Corte da Distribuição
q1 = np.percentile(array_furto, 25)
q2 = np.percentile(array_furto, 50)
q3 = np.percentile(array_furto, 75)
print('Q1:', q1)   # 25%
print('Q2:', q2)   # 50% no q2 o valor é igual ao valor da mediana calculada acima
print('Q3:', q3)   # 75%

# %%
# Aplicando os Quartis na Análise
# CISPs nos 25% com mais furtos de celular — acima de Q3
# Usando .loc
df_top25_loc = df_cisp_capital.loc[df_cisp_capital['furto_celular'] > q3]
print(df_top25_loc)
print("="*80)
# Usando .query()
df_top25_query = df_cisp_capital.query('furto_celular > @q3')
print(df_top25_query)


# %%
#filtros usando .loc  Filtragem com .loc e .query()
#  Contexto: analisar apenas a cidade do Rio de Janeiro (capital)
# Usando .loc
#df_cisp_roubo_ve = df.loc[df['munic'] == 'Rio de Janeiro']    # Seleciona somente do municipio
# EXERCICIO 01: roubo_veiculo
df_cisp_furto_ve = df.groupby('munic')['furto_veiculos'].sum().reset_index()   # Agrupa por municipio e soma os furtos de veículos
#df_cisp_furto_ve = df.groupby('cisp')['furto_veiculos'].sum().reset_index()    # Agrupa por CISP e soma os furtos de veículos
print("furtos: ","="*80)
print(df_cisp_furto_ve) 

#df_cisp_roubo_ve = df.groupby('cisp')['roubo_veiculo' ].sum().reset_index()    # Agrupa por CISP e soma os roubos de veículos
df_cisp_roubo_ve = df.groupby('munic')['roubo_veiculo' ].sum().reset_index()    # Agrupa por CISP e soma os roubos de veículos
print("roubos: ","="*80)
print(df_cisp_roubo_ve) 

# %%
# Ordenando do maior para o menor
df_cisp_furto_ve = df_cisp_furto_ve.sort_values(by='furto_veiculos', ascending=False) # organiza os dados do maior para o menor
print(df_cisp_furto_ve) 

df_cisp_roubo_ve = df_cisp_roubo_ve.sort_values(by='roubo_veiculo', ascending=False) # organiza os dados do maior para o menor
print(df_cisp_roubo_ve) 

# %%
df_cisp_roubo_ve = df_cisp_roubo_ve.sort_values(by='roubo_veiculo', ascending=False)
print(df_cisp_roubo_ve) 
print("roubos: ","="*80)
df_cisp_roubo_ve

# %%
# df_cisp_capital já foi criado no passo anterior (groupby + reset_index)
array_furto = np.array(df_cisp_roubo_ve['roubo_veiculo'])
array_furto


