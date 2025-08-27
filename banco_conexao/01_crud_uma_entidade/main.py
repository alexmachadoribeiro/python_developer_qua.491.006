# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

try:
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    class Pessoa(Base):
        __tablename__ = "pessoa"

        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        data_nascimento = Column(Date, nullable=False)
    
    Base.metadata.create_all(engine)    
except Exception as e:
    print(f"Não foi possível conectar ao banco. {e}")