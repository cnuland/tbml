from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional
from pydantic import BaseModel

from db.models import Meals


MealsInSchema = pydantic_model_creator(
    Meals, name="MealIn", exclude_readonly=True
)
MealsOutSchema = pydantic_model_creator(
    Meals, name="MealOut", exclude=["created_on"]
)
MealsDatabaseSchema = pydantic_model_creator(
    Meals, name="Meal", exclude=["created_on"]
)

class UpdateMeal(BaseModel):
    name: Optional[str]