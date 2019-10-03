from sqlalchemy.orm import sessionmaker
from models import db_engine

Session = sessionmaker(bind=db_engine)
session = Session()

