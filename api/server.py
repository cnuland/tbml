from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "https://ibml-app-tbml.apps.okd4.cjlabs.dev",
    "http://ibml-app-tbml.apps.okd4.cjlabs.dev",
    "ibml-app-tbml.apps.okd4.cjlabs.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "hello world!"
