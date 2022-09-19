from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base

# aqui colocamos "qual o banco+tipo usado://usuario:senha@host
URL = "mysql+mysqlconnector://aluno:aluno123@localhost"

Base = declarative_base()


class Pessoa(object):
    pass

def main():
    engine = create_engine(url=URL)

    insp = inspect(engine)
    db_list = insp.get_schema_names()

    # esse método serve para simplificar a abertura e fechamento de arquivos, executando o método assim que abrir
    with engine.connect() as connection:
        result_set = connection.execute("SHOW DATABASES")

        print('\n********************BANCOS********************')
        for row in result_set:
            print(row[0])

    with engine.connect() as connection:
        connection.execute("USE world")
        result_set = connection.execute("SHOW TABLES")

        print('\n********************TABELAS DE WORLD********************')
        for row in result_set:
            print(row[0])


if __name__ == "__main__":
    main()
