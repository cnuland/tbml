from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.config import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

origins = [
    "http://localhost:8080",
    "https://tbml-app-tbml.apps.okd4.cjlabs.dev",
    "http://tbml-app-tbml.apps.okd4.cjlabs.dev",
    "tbml-app-tbml.apps.okd4.cjlabs.dev",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Generate database schema
register_tortoise(app, 
                  config=TORTOISE_ORM, 
                  generate_schemas=False)

@app.get("/")
def home():
    return "hello world!"
