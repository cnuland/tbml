from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
from api.db.models import Symptoms

from db.models import JournalEntry
from schemas.journal_entry import JournalEntryOutSchema


async def get_journals():
    return await JournalEntryOutSchema.from_queryset(JournalEntry.all())


async def get_journal(journal_id) -> JournalEntryOutSchema:
    return await JournalEntryOutSchema.from_queryset_single(JournalEntry.get(id=journal_id))


async def create_journal(journal) -> JournalEntryOutSchema:
    journal_dict = journal.dict(exclude_unset=True)
    journal_obj = await JournalEntry.create(**journal_dict)
    return await JournalEntryOutSchema.from_tortoise_orm(journal_obj)


async def update_journal(journal_id, event) -> JournalEntryOutSchema:
    try:
        db_journal = await JournalEntryOutSchema.from_queryset_single(JournalEntry.get(id=journal_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Journal {journal_id} not found")

    await JournalEntry.filter(id=journal_id).update(**event.dict(exclude_unset=True))
    return await JournalEntryOutSchema.from_queryset_single(JournalEntry.get(id=journal_id))


async def delete_journal(journal_id):
    try:
        db_journal = await JournalEntryOutSchema.from_queryset_single(JournalEntry.get(id=journal_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Journal {journal_id} not found")

    deleted_count = await JournalEntry.filter(id=journal_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Journal {journal_id} not found")
    return f"Journal {journal_id} deleted"