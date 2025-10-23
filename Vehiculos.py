from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Vehiculo, VehiculoCreate, Conductor, Destino
from database import SessionDep

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

@router.post("/", response_model=Vehiculo)
async def create_vehiculo(new_vehiculo: VehiculoCreate, session: SessionDep):
    data = new_vehiculo.model_dump()
    conductor_id = data.get("conductor_id")
    destino_id = data.get("destino_id")

    conductor_db = session.get(Conductor, conductor_id)
    destino_db = session.get(Destino, destino_id)

    if not conductor_db or not destino_db:
        raise HTTPException(status_code=404, detail="Conductor o destino no encontrados")

    vehiculo = Vehiculo.model_validate(data)
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo)

    return vehiculo


@router.get("/", response_model=list[Vehiculo])
async def list_vehiculos(session: SessionDep):
    return session.exec(select(Vehiculo)).all()


@router.get("/{placa}", response_model=Vehiculo)
async def get_vehiculo(placa: str, session: SessionDep):
    vehiculo = session.get(Vehiculo, placa)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo


@router.put("/{placa}", response_model=Vehiculo)
async def update_vehiculo(placa: str, data: VehiculoCreate, session: SessionDep):
    vehiculo = session.get(Vehiculo, placa)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(vehiculo, key, value)
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo)

    return vehiculo


@router.delete("/{placa}")
async def delete_vehiculo(placa: str, session: SessionDep):
    vehiculo = session.get(Vehiculo, placa)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    session.delete(vehiculo)
    session.commit()
    return {"ok": True, "message": "Vehículo eliminado correctamente"}
