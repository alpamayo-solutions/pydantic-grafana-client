from typing import List, Optional

from .base import GrafanaBaseModel


class ServiceAccountCreateModel(GrafanaBaseModel):
    name: str
    role: Optional[str] = None
    isDisabled: Optional[bool] = None


class ServiceAccountUpdateModel(GrafanaBaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    isDisabled: Optional[bool] = None


class ServiceAccountTokenCreateModel(GrafanaBaseModel):
    name: str
    secondsToLive: Optional[int] = None
    scope: Optional[str] = None
    scopes: Optional[List[str]] = None


__all__ = [
    "ServiceAccountCreateModel",
    "ServiceAccountUpdateModel",
    "ServiceAccountTokenCreateModel",
]
