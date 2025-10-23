from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Conductor, ConductorCreate
from database import SessionDep

router = APIRouter(prefix="/conductores", tags=["Conductores"])

@router.post("/", response_model=Conductor)
async def create_conductor(new_conductor: ConductorCreate, session: SessionDep):
    conductor = Conductor.model_validate(new_conductor.model_dump())
    session.add(conductor)
    session.commit()
    session.refresh(conductor)
    return conductor


@router.get("/", response_model=list[Conductor])
async def list_conductores(session: SessionDep):
    return session.exec(select(Conductor)).all()


@router.get("/{id}", response_model=Conductor)
async def get_conductor(id: int, session: SessionDep):
    conductor = session.get(Conductor, id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")
    return conductor


@router.put("/{id}", response_model=Conductor)
async def update_conductor(id: int, data: ConductorCreate, session: SessionDep):
    conductor = session.get(Conductor, id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(conductor, key, value)
    session.add(conductor)
    session.commit()
    session.refresh(conductor)
    return conductor


@router.delete("/{id}")
async def delete_conductor(id: int, session: SessionDep):
    conductor = session.get(Conductor, id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")
    session.delete(conductor)
    session.commit()
    return {"ok": True, "message": "Conductor eliminado correctamente"}
