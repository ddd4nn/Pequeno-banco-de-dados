import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:teste123@localhost:5432/postgres')

df = pd.read_excel('Aluno.xlsx')

df.to_sql(name="Alunos", con=engine, schema="Alunos")

print(df)