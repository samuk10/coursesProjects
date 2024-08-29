from typing import Annotated

from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", examples=["João"], max_length=50)
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do atleta",
            examples=["12345678900"],
            max_length=11,
        ),
    ]
    idade: Annotated[
        PositiveFloat,
        Field(description="Idade do atleta", examples=[25], ge=0),
    ]
    peso: Annotated[
        PositiveFloat,
        Field(description="Peso do atleta", examples=[75.5], ge=0),
    ]
    altura: Annotated[
        PositiveFloat,
        Field(description="Altura do atleta", examples=[1.70], ge=0),
    ]
    sexo: Annotated[
        str,
        Field(
            description="Sexo do atleta (M - Masculino, F - Feminino)",
            examples=["M"],
            max_length=1,
        ),
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass
