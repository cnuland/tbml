from tortoise.contrib.pydantic import pydantic_model_creator

from db.models import Symptoms


SymptomsInSchema = pydantic_model_creator(
    Symptoms, name="SymptomIn", exclude_readonly=True
)
SymptomsOutSchema = pydantic_model_creator(
    Symptoms, name="SymptomOut", exclude=["created_on"]
)
SymptomsDatabaseSchema = pydantic_model_creator(
    Symptoms, name="Symptom", exclude=["created_on"]
)