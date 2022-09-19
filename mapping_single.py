from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#aqui colocamos "qual o banco+tipo usado://usuario:senha@host
URL = "mysql+mysqlconnector://aluno:aluno123@localhost/orm"

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


def main():
    engine = create_engine(url=URL)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)

    with Session.begin() as session:
        daniel = Pessoa(nome='Daniel M H Souza')
        session.add(daniel)


if __name__ == "__main__":
    main()
