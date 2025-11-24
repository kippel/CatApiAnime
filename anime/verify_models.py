import sys
import os
from sqlalchemy.orm import configure_mappers

# Add the current directory to sys.path
sys.path.append(os.getcwd())

try:
    print("Attempting to import models...")
    from app.db.models import Anime
    print("Models imported. Configuring mappers...")
    configure_mappers()
    print("SUCCESS: Models configured successfully without NoForeignKeysError.")
except Exception as e:
    print(f"FAILURE: {e}")
    sys.exit(1)
