from typing import Any, Dict, List, Optional

from .base import GrafanaBaseModel


class FolderCreateModel(GrafanaBaseModel):
    title: str
    uid: Optional[str] = None
    parentUid: Optional[str] = None


class FolderMoveModel(GrafanaBaseModel):
    parentUid: str


class FolderUpdateModel(GrafanaBaseModel):
    title: Optional[str] = None
    version: Optional[int] = None
    overwrite: Optional[bool] = None
    uid: Optional[str] = None

    def prepare_payload(self) -> Dict[str, Any]:
        data = self.to_payload()
        if "overwrite" in data and not data["overwrite"]:
            data.pop("overwrite", None)
        return data


class FolderPermissionsModel(GrafanaBaseModel):
    items: List[Dict[str, Any]]


class FolderUserPermissionsModel(GrafanaBaseModel):
    permission: Optional[str] = None


__all__ = [
    "FolderCreateModel",
    "FolderMoveModel",
    "FolderUpdateModel",
    "FolderPermissionsModel",
    "FolderUserPermissionsModel",
]
