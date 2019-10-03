from sqlalchemy.orm import sessionmaker
from vehicle.models import db_engine

Session = sessionmaker(bind=db_engine)
session = Session()
