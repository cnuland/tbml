from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.nutriments as crud
from schemas.nutriments import NutrimentsOutSchema, NutrimentsInSchema


router = APIRouter()


@router.get(
    "/nutriments",
    response_model=List[NutrimentsOutSchema]
)
async def get_nutriments():
    return await crud.get_nutriments()


@router.get(
    "/meal/{nutriment_id}",
    response_model=NutrimentsOutSchema)
async def get_nutriment(nutriment_id: int) -> NutrimentsOutSchema:
    try:
        return await crud.get_nutriment(nutriment_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Nutriment does not exist",
        )


@router.post(
    "/nutriment", response_model=NutrimentsOutSchema
)
async def create_nutriment(
    nutriment: NutrimentsInSchema
) -> NutrimentsOutSchema:
    return await crud.create_nutriment(nutriment)


@router.delete(
    "/nutriment/{nutriment_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_nutriment(
    nutriment_id: int
):
    return await crud.delete_nutriment(nutriment_id)