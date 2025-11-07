from typing import Literal

from .base import GrafanaBaseModel


class DashboardRestoreModel(GrafanaBaseModel):
    version: int


class DashboardDiffTarget(GrafanaBaseModel):
    dashboardId: int
    version: int


class DashboardDiffModel(GrafanaBaseModel):
    base: DashboardDiffTarget
    new: DashboardDiffTarget
    diffType: Literal["json", "basic"] = "json"


__all__ = [
    "DashboardRestoreModel",
    "DashboardDiffTarget",
    "DashboardDiffModel",
]
