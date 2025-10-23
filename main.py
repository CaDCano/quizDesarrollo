from fastapi import FastAPI
from database import init_db
from routers import vehiculos, conductores, destinos

app = FastAPI(title="Transportes Sigmotoa API", version="3.0")

@app.on_event("startup")
def on_startup():
    init_db()

# Registrar routers
app.include_router(vehiculos.router)
app.include_router(conductores.router)
app.include_router(destinos.router)
