from sqlalchemy import Column, String, ForeignKey, Date, Interval, create_engine, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Mac(Base):
    __tablename__ = 'mac'
    id = Column("id", Integer, primary_key=True)
    mac = Column("mac", String(32), unique=True)

class Ssid(Base):
    __tablename__ = "ssid"
    id = Column("id", Integer, primary_key=True)
    ssid = Column("ssid", String(32), unique=True)

class Mac_ssid(Base):
    __tablename__ = 'ssid_mac'
    id = Column("id", Integer, primary_key=True)
    mac_adress = Colum("mac_id", Integer, foreng_key(mac.id))
    ssid = Colum("ssid_id", Integer, foreng_key(ssid.id))

class Link(Base):
    __tablename__ = 'links'
    id = Column("id", Integer, primary_key=True)
    mac_id = Colum("device1_id", Integer, foreng_key(mac.id))
    mac2_id = Colum("device2_id", Integer, foreng_key(mac.id))

def get_engine():
    engine = create_engine(DATABASE_URI)
    return engine


def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine,expire_on_commit=False)


def init():
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)




