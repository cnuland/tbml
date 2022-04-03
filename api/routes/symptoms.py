from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.symptoms as crud
from schemas.symptoms import SymptomsOutSchema, SymptomsInSchema


router = APIRouter()


@router.get(
    "/symptoms",
    response_model=List[SymptomsOutSchema]
)
async def get_symptoms():
    return await crud.get_symptoms()


@router.get(
    "/symptom/{symptom_id}",
    response_model=SymptomsOutSchema)
async def get_symptom(symptom_id: int) -> SymptomsOutSchema:
    try:
        return await crud.get_symptom(symptom_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Symptom does not exist",
        )


@router.post(
    "/symptom", response_model=SymptomsOutSchema
)
async def create_symptom(
    symptom: SymptomsInSchema
) -> SymptomsOutSchema:
    return await crud.create_symptom(symptom)

@router.delete(
    "/symptom/{symptom_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_symptom_id(
    symptom_id: int
):
    return await crud.delete_symptoms(symptom_id)