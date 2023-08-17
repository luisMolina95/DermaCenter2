from sqlalchemy import create_engine, inspect


DATABASE_URL = "postgresql://postgres:password@db/postgres"
engine = create_engine(DATABASE_URL)
conn = engine.connect()
inspector = inspect(engine)