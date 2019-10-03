from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, session
from sqlalchemy import create_engine

Base = declarative_base()
DB_URI = 'postgresql+psycopg2://postgres:postgres@localhost/SampleDB'

association_table = Table("users_to_cars", Base.metadata,

                          Column("user_id", Integer, ForeignKey("vehicle_users.id")),
                          Column("car_id", Integer, ForeignKey("vehicle_cars.id")))


class User(Base):
    __tablename__ = "vehicle_users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    # cars = relationship("Car", secondary=association_table, backref="users")


class Car(Base):
    __tablename__ = "vehicle_cars"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    users = relationship("User", secondary=association_table, backref="cars")


db_engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/SampleDB')
Base.metadata.create_all(db_engine)
