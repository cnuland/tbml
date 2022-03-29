from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from db.models import Nutriments
from schemas.nutriments import NutrimentsOutSchema


async def get_nutriments():
    return await NutrimentsOutSchema.from_queryset(Nutriments.all())


async def get_nutriment(nutriment_id) -> NutrimentsOutSchema:
    return await NutrimentsOutSchema.from_queryset_single(Nutriments.get(id=nutriment_id))


async def create_nutriment(meal) -> NutrimentsOutSchema:
    meal_dict = meal.dict(exclude_unset=True)
    meal_obj = await Nutriments.create(**meal_dict)
    return await NutrimentsOutSchema.from_tortoise_orm(meal_obj)


async def update_nutriment(nutriment_id, meal) -> NutrimentsOutSchema:
    try:
        db_nutriment = await NutrimentsOutSchema.from_queryset_single(Nutriments.get(id=nutriment_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Nutriment {nutriment_id} not found")

    await Nutriments.filter(id=nutriment_id).update(**meal.dict(exclude_unset=True))
    return await NutrimentsOutSchema.from_queryset_single(Nutriments.get(id=nutriment_id))


async def delete_nutriment(nutriment_id):
    try:
        db_nutriment = await NutrimentsOutSchema.from_queryset_single(Nutriments.get(id=nutriment_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Nutriment {nutriment_id} not found")

    deleted_count = await Nutriments.filter(id=nutriment_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Nutriment {nutriment_id} not found")
    return f"Deleted Nutriment {nutriment_id}"