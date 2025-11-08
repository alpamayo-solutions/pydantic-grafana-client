from typing import List

from .base import GrafanaBaseModel


class TeamRoleAssignmentModel(GrafanaBaseModel):
    roleUid: str


class TeamRolesReplaceModel(GrafanaBaseModel):
    roleUids: List[str]


__all__ = [
    "TeamRoleAssignmentModel",
    "TeamRolesReplaceModel",
]
