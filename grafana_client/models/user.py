from typing import Optional

from .base import GrafanaBaseModel


class UserUpdateModel(GrafanaBaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    login: Optional[str] = None
    theme: Optional[str] = None
    timezone: Optional[str] = None
    password: Optional[str] = None
    isDisabled: Optional[bool] = None
    role: Optional[str] = None


class UserPasswordChangeModel(GrafanaBaseModel):
    oldPassword: str
    newPassword: str
    confirmNew: Optional[str] = None

    def prepare_payload(self):
        data = self.to_payload()
        if data.get("confirmNew") is None:
            data["confirmNew"] = data["newPassword"]
        return data


class UserOrganizationAssignmentModel(GrafanaBaseModel):
    loginOrEmail: str
    role: str


class UserOrganizationRoleModel(GrafanaBaseModel):
    role: str


class UserAuthTokenRevokeModel(GrafanaBaseModel):
    authTokenId: int


__all__ = [
    "UserUpdateModel",
    "UserPasswordChangeModel",
    "UserOrganizationAssignmentModel",
    "UserOrganizationRoleModel",
    "UserAuthTokenRevokeModel",
]
