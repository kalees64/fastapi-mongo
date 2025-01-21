import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    if not client:
        print(f'-- DB Not Connected')
    print(f'-- DB Connected Successfully')
    database = client[os.getenv("DATABASE_NAME")]
except Exception as e:
    print(f'-- DB Connection Error : {e}')