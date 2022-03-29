from tortoise.contrib.pydantic import pydantic_model_creator

from db.models import Nutriments


NutrimentsInSchema = pydantic_model_creator(
    Nutriments, name="NutrimentIn", exclude_readonly=True
)
NutrimentsOutSchema = pydantic_model_creator(
    Nutriments, name="NutrimentOut", exclude=["created_on"]
)
NutrimentsDatabaseSchema = pydantic_model_creator(
    Nutriments, name="Nutriment", exclude=["created_on"]
)