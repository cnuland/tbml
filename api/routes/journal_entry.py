from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.journal_entry as crud
from schemas.journal_entry import JournalEntryOutSchema, JournalEntryInSchema, UpdateJournalEntry


router = APIRouter()


@router.get(
    "/journals",
    response_model=List[JournalEntryOutSchema]
)
async def get_journals():
    return await crud.get_journals()


@router.get(
    "/journal/{journal_id}",
    response_model=JournalEntryOutSchema)
async def get_event(journal_id: int) -> JournalEntryOutSchema:
    try:
        return await crud.get_journal(journal_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Journal does not exist",
        )


@router.post(
    "/journal", response_model=JournalEntryOutSchema
)
async def create_journal(
    journal: JournalEntryInSchema
) -> JournalEntryOutSchema:
    return await crud.create_journal(journal)


@router.patch(
    "/journal/{journal_id}",
    response_model=JournalEntryOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_journal(
    journal_id: int,
    journal: UpdateJournalEntry,
) -> JournalEntryOutSchema:
    return await crud.update_journal(journal_id, journal)


@router.delete(
    "/journal/{journal_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_journal(
    journal_id: int
):
    return await crud.delete_journal(journal_id)