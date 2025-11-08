from typing import Any, Dict, Optional

from .base import GrafanaBaseModel


class SnapshotCreateModel(GrafanaBaseModel):
    dashboard: Dict[str, Any]
    name: Optional[str] = None
    expires: Optional[int] = None
    external: Optional[bool] = None
    key: Optional[str] = None
    deleteKey: Optional[str] = None

    def prepare_payload(self) -> Dict[str, Any]:
        data = self.to_payload()
        return {key: value for key, value in data.items() if value is not None}


__all__ = ["SnapshotCreateModel"]
