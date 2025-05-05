from sqlalchemy.ext.declarative import declarative_base
from xmlrpc.client import boolean
from sqlalchemy import Boolean, Table, Column, Integer, String
# from database import metadata

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("author", String(100)),
    Column("year", Integer),
)


client = Table(
    "client",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("source",String(100)),
    Column("destination",String(100)),
    Column("noOfDdays",Integer),
    Column("TravelPreference",String(100)),
    Column("AccPreference",String(100)),
    Column("FoodSuggestion",Boolean),
    Column("Sightseeing",Integer)
)


transport = Table(
    "transport1",
    metadata,
    Column("S.No",Integer,primary_key=True),
    Column("Tname",String(100)),
    Column("Ttype",String(100)),
    Column("Tdepa",String(100)),
    Column("Tarr",String(100)),
    Column("Tsrc",String(100)),
    Column("Tdura",String(100)),
    Column("Tdes",String(100)),
    Column("Tprice",String(100)),
    Column("Tfrequency",String(100)),
    Column("TypeofRoute",String(100))
)


