import uvicorn #type: ignore
from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
  AUTHOR: str
  
  class Config:
    env_file = ".env"


def main():
  settings = Settings()
  print(settings.AUTHOR) # debugging log
  uvicorn.run("backend.app:app", host="localhost", port=8000, reload=True)


if __name__ == "__main__":
  main()