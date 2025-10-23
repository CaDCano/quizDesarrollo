from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Destino, DestinoCreate
from database import SessionDep

router = APIRouter(prefix="/destinos", tags=["Destinos"])

@router.post("/", response_model=Destino)
async def create_destino(new_destino: DestinoCreate, session: SessionDep):
    destino = Destino.model_validate(new_destino.model_dump())
    session.add(destino)
    session.commit()
    session.refresh(destino)
    return destino


@router.get("/", response_model=list[Destino])
async def list_destinos(session: SessionDep):
    return session.exec(select(Destino)).all()


@router.get("/{id}", response_model=Destino)
async def get_destino(id: int, session: SessionDep):
    destino = session.get(Destino, id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return destino


@router.put("/{id}", response_model=Destino)
async def update_destino(id: int, data: DestinoCreate, session: SessionDep):
    destino = session.get(Destino, id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(destino, key, value)
    session.add(destino)
    session.commit()
    session.refresh(destino)
    return destino


@router.delete("/{id}")
async def delete_destino(id: int, session: SessionDep):
    destino = session.get(Destino, id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    session.delete(destino)
    session.commit()
    return {"ok": True, "message": "Destino eliminado correctamente"}
