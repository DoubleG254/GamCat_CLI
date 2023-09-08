from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///games.db")
Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    developer_id = Column(String, ForeignKey("developer.id"))
    developer = relationship("Developer", back_populates="games")
    genre = relationship("Genre", back_populates="games")

class Developer(Base):
    __tablename__ = "developer"

    id = Column(String, primary_key=True)
    name = Column(String)
    total_games = Column(Integer)
    games = relationship("Game", back_populates="developer")
    
class Genre(Base):
    __tablename__ = "genre"

    id = Column(String, primary_key=True)
    name = Column(String)

    games = relationship("Game", back_populates="genre")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

