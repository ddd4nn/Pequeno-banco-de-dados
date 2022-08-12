# Pequeno banco de dados
Este projeto é um projeto de **estudo** de bancos de dados utilizando as tecnologias: **Python, Docker, SQL,  PostgreSQL, Pandas, Dbeaver, csv e xlsx**.

O objetivo é bem simples. Alimentar o banco de dados com arquivos .CSV e .XLSX, e poder fazer consultas em SQL.

Aqui temos um exemplo de arquivo xlsx a ser enviado para o banco. <br>
![planilha](https://i.imgur.com/6JbD7LR.png) <br>

Primeiramente devemos ligar o banco utilizando **PostgreSQL** em **Docker** <br>
executa-se o comando:
```
sudo docker run -e POSTGRES_PASSWORD=teste123 -p 5432:5432 postgres 
``` 
<br>
Tem-se então o output: <br>

![Docker](https://i.imgur.com/CjR6r4B.png)<br>

Para acessar a interface gráfica do banco, utlizei o **Dbeaver**:<br>

![Dbeaver](https://i.imgur.com/lNQrO4n.png)<br>

Agora devemos alimentar o banco com o dados da planilha utilizando **Pandas**.<br>

Codigo **Python** utilizando a biblioteca **Pandas** para o envio dos dados:
```
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:teste123@localhost:5432/postgres')

df = pd.read_excel('Aluno.xlsx')

df.to_sql(name="Alunos", con=engine, schema="Alunos")

print("Dados enviados com sucesso!")

```
Output:<br>

![output python](https://i.imgur.com/vn7qZMa.png)<br>

Após isso, os dados devem aparecer no banco.<br>
![dados no banco](https://i.imgur.com/CmtVg2z.png)<br>

Para consultar informações no banco, utilizaremos **SQL**:
```
select 
"Nome" 
from 
"Alunos"
where
"Classe" > 2
```
Onde procuramos o nome dos alunos que estão acima do segundo semestre. O output é:<br>
![Consulta SQL](https://i.imgur.com/49HqzfN.png)<br>

E então temos os nomes dos nossos alunos:<br>
![Consulta SQL](https://i.imgur.com/POX8GG3.png)<br>

Podemos consultar o banco com vários outros filtros, cabe apenas a quem quer colher a informação.



# Autor
---

<a href="https://github.com/ddd4nn">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/92939580?s=400&u=290918d17416ffa5cf5e3b6f5e60162e7f568ff8&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Danilo Acosta</b></sub></a> <a https://avatars.githubusercontent.com/u/92939580?s=400&u=290918d17416ffa5cf5e3b6f5e60162e7f568ff8&v=4" title="Danilo">🚀</a>


Feito por Danilo Acosta 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Danilo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/danilo-acosta/)](https://www.linkedin.com/in/danilo-acosta/) 
[![Gmail Badge](https://img.shields.io/badge/-acostadanilo34@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:acostadanilo34@gmail.com)](mailto:acostadanilo34@gmail.com)
