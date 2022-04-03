from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.events as crud
from schemas.events import EventsOutSchema, EventsInSchema, UpdateEvent


router = APIRouter()


@router.get(
    "/events",
    response_model=List[EventsOutSchema]
)
async def get_events():
    return await crud.get_events()


@router.get(
    "/event/{event_id}",
    response_model=EventsOutSchema)
async def get_event(event_id: int) -> EventsOutSchema:
    try:
        return await crud.get_event(event_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Event does not exist",
        )


@router.post(
    "/event", response_model=EventsOutSchema
)
async def create_event(
    event: EventsInSchema
) -> EventsOutSchema:
    return await crud.create_event(event)


@router.patch(
    "/event/{event_id}",
    response_model=EventsOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_event(
    event_id: int,
    event: UpdateEvent,
) -> EventsOutSchema:
    return await crud.update_event(event_id, event)


@router.delete(
    "/event/{event_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_event(
    event_id: int
):
    return await crud.delete_event(event_id)