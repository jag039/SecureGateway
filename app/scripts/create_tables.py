from app.database.db import Base, engine
from app.models.token import TokenizedData  # noqa: F401

print("⏳ Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created.")
