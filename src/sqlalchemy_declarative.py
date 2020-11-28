import sqlalchemy
from sqlalchemy import (Column, VARCHAR, ForeignKey, Date, Float, Integer,
                        create_engine)
from sqlalchemy.engine import base
from sqlalchemy.ext.declarative import (declarative_base)

Base = declarative_base()


class Continents(Base):
    __tablename__ = 'continents'
    idc = Column('idc', Integer, primary_key=True, autoincrement=True)
    continent = Column('continent', VARCHAR(20), nullable=False)


class Countries(Base):
    __tablename__ = 'countries'
    idl = Column('idl', Integer, primary_key=True)
    location = Column('location', VARCHAR(30), nullable=False)
    idc = Column('idc', Integer, ForeignKey("continents.idc",
                                            ondelete='RESTRICT',
                                            onupdate='CASCADE'))


class Cases(Base):
    __tablename__ = 'cases'
    id = Column('id', Integer, primary_key=True)
    idl = Column('idl', ForeignKey('countries.idl', ondelete='RESTRICT',
                                   onupdate='CASCADE'),
                 nullable=False)
    dates = Column('dates', Date, nullable=False)
    new_tests = Column('new_tests', Float, nullable=False)
    new_cases = Column('new_cases', Float, nullable=False)
    new_deaths = Column('new_deaths', Float, nullable=False)
    total_tests = Column('total_tests', Float, nullable=False)
    total_cases = Column('total_cases', Float, nullable=False)
    total_deaths = Column('total_deaths', Float, nullable=False)


def create_database(db_name: str, echo: bool = True) -> base.Engine:
    engine = create_engine(f'sqlite:///{db_name}', echo=echo)
    engine.execute('PRAGMA foreign_keys = ON;')
    Base.metadata.create_all(engine)
    return engine
