import os
import time

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Base
import logging
from fill_db import fill_initial_data


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class DatabaseManager:
    def __init__(self):
        self.DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
        self.engine = create_engine(self.DATABASE_URL)
        time.sleep(5)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        fill_initial_data(self.session)
