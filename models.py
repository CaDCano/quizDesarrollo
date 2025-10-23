from sqlmodel import SQLModel, Field, Relationship

class VehiculosBase(SQLModel):
    tipoVehiculo: str | None = Field(default=None)
    color: str | None = Field(default=None)
    modelo: int | None = Field(default=None)
    status: bool | None = Field(default=False)


class DestinoBase(SQLModel):
    ciudad: str | None = Field(default="Bogotá")
    barrio: str | None = Field(default=None)
    localidad: str | None = Field(default=None)
    calle: int | None = Field(default=None)
    descripcion: str | None = Field(default=None)


class ConductorBase(SQLModel):
    nombre: str | None = Field(default=None)
    telefono: int | None = Field(default=None)
    status: bool | None = Field(default=True)


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


class VehiculoCreate(VehiculosBase):
    placa: str
    conductor_id: int
    destino_id: int


class ConductorCreate(ConductorBase):
    id: int


class DestinoCreate(DestinoBase):
    pass

