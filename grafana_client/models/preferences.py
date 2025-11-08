import dataclasses
from typing import Optional


@dataclasses.dataclass
class PersonalPreferences:
    """
    Request/response model for user-, team- and organization-preferences.

    https://grafana.com/docs/grafana/latest/developers/http_api/preferences/
    """

    homeDashboardId: Optional[int] = None
    homeDashboardUID: Optional[str] = None
    locale: Optional[str] = None
    theme: Optional[str] = None
    timezone: Optional[str] = None
    weekStart: Optional[str] = None

    def asdict(self, filter_none: bool = False):
        if filter_none:
            return dataclasses.asdict(self, dict_factory=self.dict_factory_filter_none)
        return dataclasses.asdict(self)

    @staticmethod
    def dict_factory_filter_none(seq=None, **kwargs):
        seq = [item for item in seq if item[1] is not None]
        data = dict(seq)
        data.update(kwargs)
        return data


__all__ = [
    "PersonalPreferences",
]
