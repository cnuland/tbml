from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional
from pydantic import BaseModel

from db.models import Events


EventsInSchema = pydantic_model_creator(
    Events, name="EventIn", exclude_readonly=True
)
EventsOutSchema = pydantic_model_creator(
    Events, name="EventOut", exclude=["created_on", "journal_entry.created_on"]
)
EventsDatabaseSchema = pydantic_model_creator(
    Events, name="Event", exclude=["created_on", "journal_entry.created_on"]
)

class UpdateEvent(BaseModel):
    name: Optional[str]
    description: Optional[str]