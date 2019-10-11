from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
DB_URI = 'postgresql+psycopg2://postgres:postgres@localhost/DataDB'

states_projects = Table("states_projects", Base.metadata,

                        Column("state_id", Integer, ForeignKey("data_states.id")),
                        Column("project_id", Integer, ForeignKey("data_projects.id")))


class Project(Base):
    __tablename__ = "data_projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    states = relationship("State", secondary=states_projects, back_populates="projects")


states_violations = Table("states_violations", Base.metadata,

                          Column("state_id", Integer, ForeignKey("data_states.id")),
                          Column("violation_id", Integer, ForeignKey("data_violations.id")))


class Violation(Base):
    __tablename__ = "data_violations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    states = relationship("State", secondary=states_violations, back_populates="violations")


states_folders = Table("states_folders", Base.metadata,

                       Column("state_id", Integer, ForeignKey("data_states.id")),
                       Column("folder_id", Integer, ForeignKey("data_folders.id")))


class Folder(Base):
    __tablename__ = "data_folders"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    states = relationship("State", secondary=states_folders, back_populates="folders")


class Dashboard(Base):
    __tablename__ = "data_dashboards"
    id = Column(Integer, primary_key=True)
    summary = Column(String)
    state_id = Column(Integer, ForeignKey("data_states.id"))
    states = relationship("State", back_populates="dashboard")


states_rules = Table("states_rules", Base.metadata,

                     Column("state_id", Integer, ForeignKey("data_states.id")),
                     Column("rule_id", Integer, ForeignKey("data_rules.id")))


class Rule(Base):
    __tablename__ = "data_rules"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    states = relationship("State", secondary=states_rules, back_populates="rules")


class State(Base):
    __tablename__ = "data_states"
    id = Column(Integer, primary_key=True)
    record_time = Column(String)
    compare_time = Column(String)
    projects = relationship("Project", secondary=states_projects, back_populates="states")
    violations = relationship("Violation", secondary=states_violations, back_populates="states")
    folders = relationship("Folder", secondary=states_folders, back_populates="states")
    rules = relationship("Rule", secondary=states_rules, back_populates="states")
    dashboard = relationship("Dashboard", uselist=False, back_populates="states")


db_engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/DataDB')
Base.metadata.create_all(db_engine)
