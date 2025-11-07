from typing import Any, Dict, List, Optional

from .base import GrafanaBaseModel


class AnnotationModel(GrafanaBaseModel):
    dashboardId: Optional[int] = None
    dashboardUID: Optional[str] = None
    panelId: Optional[int] = None
    time: Optional[int] = None
    timeEnd: Optional[int] = None
    tags: Optional[List[str]] = None
    text: Optional[str] = None

    def prepare_payload(self) -> Dict[str, Any]:
        data = self.to_payload()
        if "tags" not in data or data["tags"] is None:
            data["tags"] = []
        return data


class AnnotationGraphiteModel(GrafanaBaseModel):
    what: Optional[str] = None
    tags: Optional[List[str]] = None
    when: Optional[int] = None
    data: Optional[str] = None

    def prepare_payload(self) -> Dict[str, Any]:
        data = self.to_payload()
        if "tags" not in data or data["tags"] is None:
            data["tags"] = []
        return data


__all__ = [
    "AnnotationModel",
    "AnnotationGraphiteModel",
]
