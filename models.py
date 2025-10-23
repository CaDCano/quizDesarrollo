from sqlmodel import SQLModel, Field, Relationship
from utils import Kind

class VehiculosBase(SQLModel):
    tipoVehiculo: str | None = Field(description="Tipo de vehiculo")
    color: str | None = Field(description="Color del vehiculo", default=None)
    modelo: int | None = Field(description="Modelo del vehiculo", default=None)
    status: bool | None = Field(description="Esta en funcionamiento el vehiculo", default=False)
    

class DestinoBase(SQLModel):
    ciudad: str | None = Field(description="Ciudad de destino", default="Bogota")
    barrio: str | None = Field(description="Barrio de destino")
    localidad: str| None = Field(description="Localidad de destino")
    calle: int| None = Field(description="Calle de destino")
    descripcion: str| None = Field(description="Descripcion del destino")


class ConductorBase(SQLModel):
    nombre:str | None = Field(description="Calle de destino")
    telefono: int | None = Field(description="Calle de destino")
    status: bool | None = Field(description="El conductor esta en servicio?", default=True)

class Vehiculo(VehiculosBase, table = True):
    placa: str | None = Field(default=None,primary_key=True )
    Conductor_id: int = Relationship(foreign_key ="conductor.id"primary_key=True)
    destino_id: int | None = Field(default=None,foreign_key="destino.id",primary_key=True)

class conductor(ConductorBase, table=True):
    id:int | None = Field(description="Cedudla del conductor", primary_key=True)

class destino(DestinoBase, table=True):
    id:int | None = Field(description="Id del destino del vehiculo",primary_key=True)


