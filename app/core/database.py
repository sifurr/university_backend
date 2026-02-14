from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


# Create db engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False # Production safe (no SQL log)
)

# Session factory
Sessionlocal = sessionmaker(
    autocommit=False, # manual commit -> atomicity
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    """
    One DB session per request.
    Ensures:
    - commit if success
    - rollback if error
    """
    db = Sessionlocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
    