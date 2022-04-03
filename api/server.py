from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from db.config import TORTOISE_ORM
from db.register import register_tortoise

from routes import meals, journal_entry, nutriments, symptoms, events

Tortoise.init_models(["db.models"], "models")

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

app.include_router(meals.router)
app.include_router(nutriments.router)
app.include_router(events.router)
app.include_router(symptoms.router)
app.include_router(journal_entry.router)

# Generate database schema
register_tortoise(app, 
                  config=TORTOISE_ORM, 
                  generate_schemas=False)

@app.get("/")
def home():
    return "hello world!"
