from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from db.models import Symptoms
from schemas.symptoms import SymptomsOutSchema


async def get_symptoms():
    return await SymptomsOutSchema.from_queryset(Symptoms.all())


async def get_symptom(symptom_id) -> SymptomsOutSchema:
    return await SymptomsOutSchema.from_queryset_single(Symptoms.get(id=symptom_id))


async def create_symptom(symptom) -> SymptomsOutSchema:
    symptom_dict = symptom.dict(exclude_unset=True)
    symptom_obj = await Symptoms.create(**symptom_dict)
    return await SymptomsOutSchema.from_tortoise_orm(symptom_obj)


async def update_symptom(symptom_id, symptom) -> SymptomsOutSchema:
    try:
        db_symptom = await SymptomsOutSchema.from_queryset_single(Symptoms.get(id=symptom_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Symptom {symptom_id} not found")

    await Symptoms.filter(id=symptom_id).update(**symptom.dict(exclude_unset=True))
    return await SymptomsOutSchema.from_queryset_single(Symptoms.get(id=symptom_id))


async def delete_symptoms(symptom_id):
    try:
        db_symptoms = await SymptomsOutSchema.from_queryset_single(Symptoms.get(id=symptom_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Symptom {symptom_id} not found")

    deleted_count = await Symptoms.filter(id=symptom_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Symptom {symptom_id} not found")
    return f"Symptom {symptom_id} deleted"