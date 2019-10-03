from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
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

    def __repr__(self):
        return "<Note(title='%s', description='%s', created_at='%s',created_by='%s,priority='%s')>" % (self.title,
            self.description, self.created_at,self.created_by,self.priority)


# if __name__ == "__main__":
#
#
#     engine = create_engine(DB_URI)
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add_all([
#     Note(title='Motivation',description='Motivation is the primary gole',created_at='AP',created_by='APJ',
#          priority='01'),
#     Note(title='Inspiration',description='Inspiration is the responsibile gole',created_at='AP',created_by='APJ',
#          priority='01')])
#
# session.commit()
