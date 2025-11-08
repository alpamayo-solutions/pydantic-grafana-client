from typing import Optional

from .base import GrafanaBaseModel


class OrganizationCreateModel(GrafanaBaseModel):
    name: str


class OrganizationUpdateModel(GrafanaBaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    zipCode: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None


class OrganizationUserCreateModel(GrafanaBaseModel):
    loginOrEmail: str
    role: str


class OrganizationUserUpdateModel(GrafanaBaseModel):
    role: str


__all__ = [
    "OrganizationCreateModel",
    "OrganizationUpdateModel",
    "OrganizationUserCreateModel",
    "OrganizationUserUpdateModel",
]
