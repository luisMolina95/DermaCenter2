import os
from sqlalchemy import create_engine, inspect


engine = create_engine(os.environ.get('DATABASE_URL'))
conn = engine.connect()
inspector = inspect(engine)