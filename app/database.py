from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from sqlalchemy.engine import URL
import psycopg2
from psycopg2.extras import RealDictCursor
import time

connect_url = f'postgresql://{settings.database_username}:{settings.database_password}@' \
              f'{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(connect_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# connect_url = URL.create(
#     'postgresql',
#     username=credentials['username'],
#     password=credentials['password'],
#     host=credentials['host'],
#     port=credentials['port'],
#     database=credentials['database']
# )

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',
#                                 database='fastapi',
#                                 user='postgres',
#                                 password='iop123JKL',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database conn was successful')
#         break
#     except Exception as e:
#         print('Connection failed')
#         print('Error:', e)
#         time.sleep(2)