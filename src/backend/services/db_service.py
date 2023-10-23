from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from constants.postgres_constants import *

engine = create_engine(f"postgresql://{HOST}:{PORT}/{DATABASE}?user={USER}&password={PASSWORD}")

SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)
Base = declarative_base()