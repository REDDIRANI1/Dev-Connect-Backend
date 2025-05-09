from fastapi import FastAPI
from routes import auth
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routes import profile
from routes import project
from routes import comment
from routes import search

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","https://dev-connect-frontend-wv22.vercel.app"],  # You can restrict this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(project.router)
app.include_router(comment.router)
app.include_router(search.router)