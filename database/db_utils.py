from database.db_setup import SessionLocal


def get_db():
    """ Get DB """
    database = SessionLocal()

    try:
        yield database

    except:
        database.close()

