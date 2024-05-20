from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


CONN = "sqlite:///cadastro1.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)


Base.metadata.create_all(engine)
