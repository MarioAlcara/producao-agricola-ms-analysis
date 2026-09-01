import pandas as pd
from sqlalchemy import create_engine

# 1. Conexão PostgreSQL
engine = create_engine('postgresql://postgres:123456@localhost:5432/Agro_levantamento')

# 2. Ler a planilha pulando o cabeçalho descritivo do IBGE
df = pd.read_excel('Tabela_Agro_MS.xlsx', skiprows=3)

# 3. Limpar nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# 4. Enviar para o PostgreSQL
df.to_sql('tb_producao_agricola', con=engine, if_exists='replace', index=False)

print("CARGA DE DADOS AGRICOLAS CONCLUIDA COM SUCESSO!")