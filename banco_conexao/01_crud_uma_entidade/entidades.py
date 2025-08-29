from sqlalchemy import Column, Integer, String, Date

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)
        
        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar ao banco. {e}")