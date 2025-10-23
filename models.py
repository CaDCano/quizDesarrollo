# models
from sqlmodel import SQLModel, Field, Relationship


class VehiculosBase(SQLModel):
    tipoVehiculo: str | None = Field(default=None, description="Tipo de vehiculo")
    color: str | None = Field(default=None, description="Color del vehiculo")
    modelo: int | None = Field(default=None, description="Modelo del vehiculo")
    status: bool | None = Field(default=False, description="aEsta en funcionamiento el vehiculo?")


class DestinoBase(SQLModel):
    ciudad: str | None = Field(default="Bogota", description="Ciudad de destino")
    barrio: str | None = Field(default=None, description="Barrio de destino")
    localidad: str | None = Field(default=None, description="Localidad de destino")
    calle: int | None = Field(default=None, description="Calle de destino")
    descripcion: str | None = Field(default=None, description="Descripcion del destino")


class ConductorBase(SQLModel):
    nombre: str | None = Field(default=None, description="Nombre del conductor")
    telefono: int | None = Field(default=None, description="Teléfono del conductor")
    status: bool | None = Field(default=True, description="El conductor está en servicio?")


class Destino(DestinoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    vehiculos: list["Vehiculo"] = Relationship(back_populates="destino")


class Conductor(ConductorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    vehiculos: list["Vehiculo"] = Relationship(back_populates="conductor")


class Vehiculo(VehiculosBase, table=True):
    placa: str | None = Field(default=None, primary_key=True)
    conductor_id: int | None = Field(default=None, foreign_key="conductor.id")
    destino_id: int | None = Field(default=None, foreign_key="destino.id")

    conductor: Conductor | None = Relationship(back_populates="vehiculos")
    destino: Destino | None = Relationship(back_populates="vehiculos")


