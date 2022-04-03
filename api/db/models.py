from enum import Enum
from tortoise import fields, models

class NutrimentType(str, Enum):
    Liquid = "Liquid"
    Food = "Food"

class Nutriments(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    nutriment_type = fields.CharEnumField(NutrimentType, default=NutrimentType.Food, required=True)
    carbs_gm = fields.IntField(null=True)
    protein_gm = fields.IntField(null=True)
    calories = fields.IntField(null=True, required=True)
    sugar_gm = fields.IntField(null=True)
    ounces = fields.IntField(null=True) # Only appliciable if a liquid

class Meals(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    nutriments = fields.ManyToManyField("models.Nutriments", related_name='meals', through='nutriments_in_meal')

class Symptoms(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)

class JournalEntry(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    entry = fields.TextField(required=True)
    health_rating = fields.SmallIntField(default=0)
    symptoms = fields.ManyToManyField("models.Symptoms", related_name='journal_entry', through='symptoms_in_journal')
    
class Events(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    description = fields.TextField(required=True)
    journal_entry = fields.ForeignKeyField("models.JournalEntry", related_name="journal_entry", required=True)
    
class Activities(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, required=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    time_of = fields.DatetimeField(auto_now_add=True)
    time_spent_min = fields.IntField(default=0, required=True)
    time_spent_min = fields.SmallIntField(default=0, required=True)