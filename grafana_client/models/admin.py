from typing import Dict, Union

from ..util import as_bool
from .base import GrafanaBaseModel


class AdminCreateUser(GrafanaBaseModel):
    name: str
    email: str
    login: str
    password: str


class AdminChangePassword(GrafanaBaseModel):
    password: str


class AdminChangePermissions(GrafanaBaseModel):
    isGrafanaAdmin: bool


class AdminPauseAlerts(GrafanaBaseModel):
    paused: Union[bool, str]

    def prepare_payload(self) -> Dict[str, bool]:
        data = self.to_payload()
        value = data.get("paused")
        if isinstance(value, str):
            try:
                data["paused"] = as_bool(value)
            except ValueError:
                pass
        return data


__all__ = [
    "AdminCreateUser",
    "AdminChangePassword",
    "AdminChangePermissions",
    "AdminPauseAlerts",
]
