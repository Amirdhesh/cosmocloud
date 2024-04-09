from fastapi import FastAPI
from app.api import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Library Management System",
    contact={
        "name": "Amirdhesh",
        "url": "https://amirdhesh.onrender.com/",
        "email": "amirdhesh.s2021ai@sece.ac.in",
    },
    description="Library Management System api built using FastAPI and MongoDB as a database.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api)



