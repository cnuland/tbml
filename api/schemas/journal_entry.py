from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional
from pydantic import BaseModel

from db.models import JournalEntry


JournalEntryInSchema = pydantic_model_creator(
    JournalEntry, name="JournalEntryIn", exclude_readonly=True
)
JournalEntryOutSchema = pydantic_model_creator(
    JournalEntry, name="JournalEntryOut", exclude=["created_on"]
)
JournalEntryDatabaseSchema = pydantic_model_creator(
    JournalEntry, name="JournalEntry", exclude=["created_on"]
)

class UpdateJournalEntry(BaseModel):
    name: Optional[str]
    entry: Optional[str]
    health_rating: Optional[int]