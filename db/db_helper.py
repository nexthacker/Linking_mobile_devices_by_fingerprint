from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


Base = declarative_base()


class MacAdress(Base):
    __tablename__ = "mac"

    id = Column("id", Integer, primary_key=True)
    mac = Column("mac", String(32), unique=True)


class SsidTable(Base):
    __tablename__ = "ssid"
    id = Column("id", Integer, primary_key=True)
    ssid = Column("ssid", String(32), unique=True)


class Mac_ssid(Base):
    __tablename__ = "ssid_mac"
    id = Column("id", Integer, primary_key=True)
    mac_adress = Column("mac_adress", String(32))
    ssid = Column("ssid_id", String(32))


class Link(Base):
    __tablename__ = "links"
    id = Column("id", Integer, primary_key=True)
    mac_id = Column("device1_id", String(32))
    mac2_id = Column("device2_id", String(32))
    jaccard_score = Column("jaccard_score", float)
    adamic_score = Column("adamic_score", float)
    mod_adamic_score = Column("mod_adamic_score", float)
    idf_score = Column("idf_score", float)
    idf_similarity_score = Column("idf_similarity_score", float)


def get_engine():
    user = "root"
    password = "root"
    address = "localhost"
    database_name = "ssid_mac"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)
    # engine = create_engine('mysql+pymysql://%s:%s@%s:3000/%s' %(user, password, address, database_name), echo=True)

    return engine


def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine,expire_on_commit=False)


def init(drop_tables=True):
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
    if drop_tables:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)




