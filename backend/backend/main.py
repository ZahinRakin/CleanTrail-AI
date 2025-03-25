import uvicorn
from dotenv import load_dotenv
import os



def main():
  load_dotenv()
  uvicorn.run("backend.app:app", host="localhost", port=8000, reload=True)



if __name__ == "__main__":
  main()

