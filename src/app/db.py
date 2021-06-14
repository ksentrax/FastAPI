import os

from sqlalchemy import (Column, Integer, MetaData,
                        String, Table, create_engine)
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

organizations = Table(
    "organizations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(100)),
    Column("founded", Integer),
    Column("scope", String),
    Column("location", String(50)),
    Column("website", String),
)

database = Database(DATABASE_URL)
