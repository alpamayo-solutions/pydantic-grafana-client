from typing import Optional, Union

from .base import GrafanaBaseModel


class TeamCreateModel(GrafanaBaseModel):
    name: str
    email: Optional[str] = None
    orgId: Optional[int] = None
    avatarUrl: Optional[str] = None


class TeamUpdateModel(GrafanaBaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    orgId: Optional[int] = None
    avatarUrl: Optional[str] = None


class TeamMemberModel(GrafanaBaseModel):
    userId: Optional[Union[int, str]] = None
    userUid: Optional[str] = None

    def prepare_payload(self):
        data = self.to_payload()
        if "userId" in data and data["userId"] is not None:
            data["userId"] = str(data["userId"])
        return data


class TeamExternalGroupModel(GrafanaBaseModel):
    groupId: str


__all__ = [
    "TeamCreateModel",
    "TeamUpdateModel",
    "TeamMemberModel",
    "TeamExternalGroupModel",
]
