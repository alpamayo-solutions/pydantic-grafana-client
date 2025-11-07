from typing import Any, Dict, List, Optional, Union

from ..util import as_bool
from .base import GrafanaBaseModel


class DashboardModel(GrafanaBaseModel):
    id: Optional[int] = None
    uid: Optional[str] = None
    title: Optional[str] = None
    tags: Optional[List[str]] = None
    timezone: Optional[str] = None
    schemaVersion: Optional[int] = None
    version: Optional[int] = None
    refresh: Optional[str] = None


class DashboardUpsertRequest(GrafanaBaseModel):
    dashboard: DashboardModel
    folderId: Optional[int] = None
    folderUid: Optional[str] = None
    message: Optional[str] = None
    overwrite: Optional[Union[bool, str]] = None

    def prepare_payload(self) -> Dict[str, Any]:
        data = self.to_payload()
        meta = data.get("meta")
        if isinstance(meta, dict):
            for attribute in ("folderId", "folderUid"):
                if attribute not in data and attribute in meta and meta[attribute] is not None:
                    data[attribute] = meta[attribute]

        overwrite = data.get("overwrite")
        if isinstance(overwrite, str):
            try:
                data["overwrite"] = as_bool(overwrite)
            except ValueError:
                pass
        return data


__all__ = [
    "DashboardModel",
    "DashboardUpsertRequest",
]
