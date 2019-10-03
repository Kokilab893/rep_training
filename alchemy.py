from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/SampleDB')
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)
session = Session()
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
session.commit()
our_user = session.query(User).filter_by(name='ed').first()
print(our_user.name)
our_user
User(name='ed', fullname='Ed Jones', nickname='edsnickname')
ed_user is our_user
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
session.commit()








# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
# metadata = MetaData()
# users = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('fullname', String),)
# addresses = Table('addresses', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('user_id', None, ForeignKey('users.id')),
#     Column('email_address', String, nullable=False))
