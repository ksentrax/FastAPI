from typing import List
from fastapi import APIRouter, HTTPException

from . import crud
from .models import OrganizationSchema, OrganizationDB

router = APIRouter()


@router.post("/", response_model=OrganizationDB, status_code=201)
async def create_organization(payload: OrganizationSchema):
    organization_id = await crud.post(payload)

    response_object = {
        "id": organization_id,
        "name": payload.name,
        "founded": payload.founded,
        "scope": payload.scope,
        "location": payload.location,
        "website": payload.website,
    }
    return response_object


@router.get("/{id}/", response_model=OrganizationDB)
async def read_organization(id: int):
    organization = await crud.get(id)

    if not organization:
        raise HTTPException(status_code=404, detail="Not found")
    return organization


@router.get("/", response_model=List[OrganizationDB])
async def read_all_organizations():
    return await crud.get_all()


@router.put("/{id}/", response_model=OrganizationDB)
async def update_organization(payload: OrganizationSchema, id: int):
    organization = await crud.get(id)

    if not organization:
        raise HTTPException(status_code=404, detail="Not found")

    organization_id = await crud.put(id, payload)

    response_object = {
        "id": organization_id,
        "name": payload.name,
        "founded": payload.founded,
        "scope": payload.scope,
        "location": payload.location,
        "website": payload.website,
    }
    return response_object


@router.delete("/{id}/", response_model=OrganizationDB)
async def delete_organization(id: int):
    organization = await crud.get(id)

    if not organization:
        raise HTTPException(status_code=404, detail="Not found")

    await crud.delete(id)

    return organization
