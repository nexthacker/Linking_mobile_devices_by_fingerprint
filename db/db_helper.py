from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
    mac_adress = Column("mac_id", String(32))
    ssid = Column("ssid_id", String(32))

class Link(Base):
    __tablename__ = 'links'
    id = Column("id", Integer, primary_key=True)
    mac_id = Column("device1_id", String(32))
    mac2_id = Column("device2_id", String(32))

def get_engine():
    user = "root"
    password = ""
    address = "localhost"
    database_name = "ssid_mac"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)
    # engine = create_engine('mysql+pymysql://%s:%s@%s:3000/%s' %(user, password, address, database_name), echo=True)

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




