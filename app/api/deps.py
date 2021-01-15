from app.db.session import SessionLocal


async def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
