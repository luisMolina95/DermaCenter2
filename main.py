import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

if __name__ == "__main__":
    uvicorn.run("app.app:app", host='0.0.0.0', port=int(os.environ.get('APP_DOCKER_PORT')), reload=True)
