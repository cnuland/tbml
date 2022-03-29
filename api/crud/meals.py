from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from db.models import Meals
from schemas.meals import MealsOutSchema


async def get_meals():
    return await MealsOutSchema.from_queryset(Meals.all())


async def get_meal(meal_id) -> MealsOutSchema:
    return await MealsOutSchema.from_queryset_single(Meals.get(id=meal_id))


async def create_meal(meal) -> MealsOutSchema:
    meal_dict = meal.dict(exclude_unset=True)
    meal_obj = await Meals.create(**meal_dict)
    return await MealsOutSchema.from_tortoise_orm(meal_obj)


async def update_meal(meal_id, meal) -> MealsOutSchema:
    try:
        db_meal = await MealsOutSchema.from_queryset_single(Meals.get(id=meal_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Meal {meal_id} not found")

    await Meals.filter(id=meal_id).update(**meal.dict(exclude_unset=True))
    return await MealsOutSchema.from_queryset_single(Meals.get(id=meal_id))


async def delete_meal(meal_id):
    try:
        db_meal = await MealsOutSchema.from_queryset_single(Meals.get(id=meal_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Meal {meal_id} not found")

    deleted_count = await Meals.filter(id=meal_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Meal {meal_id} not found")
    return f"Deleted Meal {meal_id}"