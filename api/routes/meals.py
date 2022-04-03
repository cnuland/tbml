from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.meals as crud
from schemas.meals import MealsOutSchema, MealsInSchema, UpdateMeal


router = APIRouter()


@router.get(
    "/meals",
    response_model=List[MealsOutSchema]
)
async def get_meals():
    return await crud.get_meals()


@router.get(
    "/meal/{meal_id}",
    response_model=MealsOutSchema)
async def get_meal(meal_id: int) -> MealsOutSchema:
    try:
        return await crud.get_meal(meal_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Meal does not exist",
        )


@router.post(
    "/meal", response_model=MealsOutSchema
)
async def create_meal(
    meal: MealsInSchema
) -> MealsOutSchema:
    return await crud.create_meal(meal)


@router.patch(
    "/meal/{meal_id}",
    response_model=MealsOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_meal(
    meal_id: int,
    meal: UpdateMeal,
) -> MealsOutSchema:
    return await crud.update_meal(meal_id, meal)


@router.delete(
    "/meal/{meal_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_meal(
    meal_id: int
):
    return await crud.delete_meal(meal_id)