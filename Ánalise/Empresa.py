# Estrutura do Exercício
# Passo 1: Carregar e Explorar os Dados
# Carregar a base de dados chamada "cancelamentos.csv" usando a biblioteca pandas.
# Observar informações gerais da base, identificando valores nulos, colunas e tipos de dados.

import pandas as pd

# Carregar os dados
df = pd.read_csv('cancelamentos.csv')

# Exibir informações gerais
print(df.info())
print(df.describe())

# Passo 2: Análise Exploratória para Identificação de Padrões de Cancelamento
# A análise exploratória deve focar nos possíveis fatores de cancelamento.
# Utilizaremos a biblioteca plotly.express para a visualização de dados e para compreender padrões específicos de clientes que cancelaram o serviço.
# Abaixo estão algumas sugestões de análises que podem ser realizadas:
# Distribuição do Tempo como Cliente e Cancelamento: Verificar se clientes que ficam menos tempo na empresa são mais propensos a cancelar.

import plotly.express as px

fig = px.histogram(df, x='tempo_como_cliente', color='cancelou' barmode='group', title="Distribuição do Tempo como cliente")
fig.show()

# Idade vs Cancelamento: Avaliar a idade dos clientes e a taxa de cancelamento para identificar padrões.

fig = px.histogram(df, x='idade', color='cancelou' barmode='overlay', title="Distribuição de Idade e Cancelamento")
fig.show()

# Total Gasto vs Cancelamento:
# Entender a relação entre o valor gasto pelo cliente e o cancelamento, verificando se há um perfil específico de consumo entre os que cancelaram.

fig = px.box(df, x='cancelou', y='total_gasto', title="Distribuição de Total Gasto por Cancelamento")
fig.show()

# Dias de Atraso e Cancelamento: Analisar se clientes que atrasam pagamentos são mais propensos a cancelar.

fig = px.histogram (df, x='dias_atraso', color='cancelou', barmode='overlay', title="Dias de Atraso e Cancelamento")
fig.show()

# Interações com Call Center e Cancelamento: Observar se o número de ligações para o call center tem relação com o cancelamento.

fig = px.box(df, x='cancelou', y='ligacoes_callcenter', title="Número de Ligações ao Call Center e Cancelamento")
fig.show()

# Passo 3: Identificação de Perfis e Padrões de Clientes
# Baseado nas análises anteriores, identifique perfis de clientes com alta probabilidade de cancelar, tais como:

# clientes com alta frequência de atrasos.
# Clientes com menor tempo de permanència.
# Clientes que fazem uso menos frequente do serviço.
# Passo 4: Projeção de Impacto com Ações de Retenção
# Simule o impacto de mudanças nas taxas de cancelamento ao melhorar fatores específicos, como:

# Redução do número de dias de atraso.
# Melhoria no atendimento (reduzindo ligações ao call center).
# Aumentar a frequência de uso por meio de incentivos.

# Crie uma cópia do dataset e modifique essas variáveis para prever o cenário onde esses fatores são melhorados.

# Simulação de cenário onde os atrasos e ligações ao call center são reduzidos para 50% dos valores originais
df_simulacao = df.copy()
df_simulacao['dias_atraso'] = df_simulacao['dias_atraso'] * 0.5
df_simulacao['ligacoes_callcenter'] = df_simulacao['ligacoes_callcenter'] * 0.5

# Visualizar comparação do cenário simulado com o cenário atual
fig = px.histogram (df_simulacao, x='cancelou', title="Distribuição de Cancelamentos no Cenário Simulado")
fig.show()

# Passo 5: Conclusão e Recomendações
# Baseado nas análises e simulação de cenários, elabore uma conclusão sobre:

# Principais motivos de cancelamento encontrados (ex.: alta frequência de ligações ao call center, atraso em pagamentos, entre outros).
# Propostas de ação para retenção, incluindo estratégias de atendimento, incentivos ao uso e programas de fidelidade.
# Previsão de impacto, indicando o número de clientes que poderiam ser retidos e como isso afetaria a receita da empresa.