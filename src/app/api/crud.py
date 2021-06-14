from .models import OrganizationSchema
from app.db import organizations, database


async def post(payload: OrganizationSchema):
    query = organizations.insert().values(name=payload.name,
                                          founded=payload.founded,
                                          scope=payload.scope,
                                          location=payload.location,
                                          website=payload.website)
    return await database.execute(query=query)


async def get(id: int):
    query = organizations.select().where(id == organizations.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = organizations.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: OrganizationSchema):
    query = (
        organizations
        .update()
        .where(id == organizations.c.id)
        .values(name=payload.name,
                founded=payload.founded,
                scope=payload.scope,
                location=payload.location,
                website=payload.website)
        .returning(organizations.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = organizations.delete().where(id == organizations.c.id)
    return await database.execute(query=query)
