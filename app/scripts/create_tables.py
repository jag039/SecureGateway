from database.db import Base, engine
from models.token import TokenizedData

print("⏳ Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created.")