from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, tarefas, usuarios

app = FastAPI(
    title="Task Manager API",
    description="API REST para gerenciamento de tarefas com autenticação JWT",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(tarefas.router)


@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "versao": "1.0.0"}


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "healthy"}
