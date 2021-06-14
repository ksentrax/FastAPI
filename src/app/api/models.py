from pydantic import BaseModel


class OrganizationSchema(BaseModel):
    name: str
    founded: int
    scope: str
    location: str
    website: str


class OrganizationDB(OrganizationSchema):
    id: int
