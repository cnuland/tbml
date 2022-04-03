from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from db.models import Events
from schemas.events import EventsOutSchema


async def get_events():
    return await EventsOutSchema.from_queryset(Events.all())


async def get_event(event_id) -> EventsOutSchema:
    return await EventsOutSchema.from_queryset_single(Events.get(id=event_id))


async def create_event(event) -> EventsOutSchema:
    event_dict = event.dict(exclude_unset=True)
    event_obj = await Events.create(**event_dict)
    return await EventsOutSchema.from_tortoise_orm(event_obj)


async def update_event(event_id, event) -> EventsOutSchema:
    try:
        db_event = await EventsOutSchema.from_queryset_single(Events.get(id=event_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")

    await Events.filter(id=event_id).update(**event.dict(exclude_unset=True))
    return await EventsOutSchema.from_queryset_single(Events.get(id=event_id))


async def delete_event(event_id):
    try:
        db_event = await EventsOutSchema.from_queryset_single(Events.get(id=event_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")

    deleted_count = await Events.filter(id=event_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    return f"Event {event_id} deleted"