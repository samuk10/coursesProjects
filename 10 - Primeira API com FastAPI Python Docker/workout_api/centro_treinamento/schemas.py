from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            examples=["CT King"],
            max_length=20,
        ),
    ]
    Endereço: Annotated[
        str,
        Field(
            description="Endereço do Centro de Treinamento",
            examples=["Av. Paulista, 1000"],
            max_length=60,
        ),
    ]
    Proprietario: Annotated[
        str,
        Field(
            description="Proprietario do Centro de Treinamento",
            examples=["Marcos"],
            max_length=30,
        ),
    ]
