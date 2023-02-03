import os
from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# load_dotenv(find_dotenv())

class Settings:
    PROJECT_TITLE :str = "Jobboard"
    PROJECT_VERSION :str = "0.1.0"
 
    POSTGRES_USER :str =os.environ.get("POSTGRES_USER")
    # POSTGRES_USER :str =os.getenv("POSTGRES_USER","postgres")
    POSTGRES_PASSWORD =os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER :str =os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT :str =os.getenv("POSTGRES_PORT")
    POSTGRES_DB :str =os.getenv("POSTGRES_DB")
    POSTGRES_URL  = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    #load dotenv my own way


settings = Settings()