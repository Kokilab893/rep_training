from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
DB_URI ='postgresql+psycopg2://postgres:postgres@localhost/SampleDB'

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    created_at = Column(String(50))
    created_by = Column(String(50))
    priority = Column(Integer)
    books=relationship('Book')

    def __repr__(self):
        return "<Note(title='%s', description='%s', created_at='%s',created_by='%s,priority='%s')>" % (self.title,
            self.description,self.created_at,self.created_by,self.priority)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    notes_id = Column(Integer, ForeignKey('notes.id'), nullable=True)
    note = relationship('Note', back_populates='books')


    def __repr__(self):
        return "<Book(name='%s')>" % (self.name)


