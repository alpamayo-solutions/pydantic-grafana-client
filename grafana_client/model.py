import dataclasses
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from pydantic import (
    BaseModel,
    ConfigDict,
)

from .util import as_bool


@dataclasses.dataclass
class DatasourceIdentifier:
    """
    A Grafana data source can be identified by either a numerical id, an
    alphanumerical uid, or a name.
    """

    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None


@dataclasses.dataclass
class DatasourceModel:
    """
    Represent the minimum required fields to create a JSON payload suitable for
    submitting to the Grafana HTTP API.

    TODO: Field `database` will be deprecated.
          https://github.com/grafana/grafana/issues/59115
    """

    name: str
    type: str
    url: str
    access: str
    database: Optional[str] = None
    user: Optional[str] = None
    jsonData: Optional[Dict] = None
    secureJsonData: Optional[Dict] = None
    secureJsonFields: Optional[Dict] = None

    def asdict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class DatasourceHealthResponse:
    """
    Represent a response for a Grafana data source health check.

    It is a mixture of the fields of the native, server-side health check
    introduced with Grafana 9+, and the client-side implementation by
    `grafana-client`.

    - Grafana 9+ uses the fields `status` and `message`, where `status` can be
      one of `OK`, or `ERROR`.
    - `grafana-client` employs a more verbose response, including metadata
      about the requested data source item (`uid`, `type`), a boolean `success`
      flag, as well as the duration in seconds the request needed and the full
      response object.
    """

    uid: str
    type: Union[str, None]
    success: bool
    status: str
    message: str
    duration: Optional[float] = None
    response: Optional[Any] = None

    def asdict(self):
        return dataclasses.asdict(self)

    def asdict_compact(self):
        data = self.asdict()
        del data["response"]
        return data


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

    def asdict(self, filter_none=False):
        if filter_none:
            return dataclasses.asdict(self, dict_factory=self.dict_factory_filter_none)
        else:
            return dataclasses.asdict(self)

    @staticmethod
    def dict_factory_filter_none(seq=None, **kwargs):
        seq = [item for item in seq if item[1] is not None]
        data = dict(seq)
        data.update(kwargs)
        return data


TModel = TypeVar("TModel", bound="GrafanaBaseModel")


class GrafanaBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    @classmethod
    def validate(cls: Type[TModel], data: Any) -> TModel:
        if isinstance(data, cls):
            return data
        if hasattr(cls, "model_validate"):
            return cls.model_validate(data)  # type: ignore[attr-defined]
        return cls.parse_obj(data)  # type: ignore[attr-defined]

    def to_payload(self, exclude_none: bool = True) -> Dict[str, Any]:
        if hasattr(self, "model_dump"):
            return self.model_dump(by_alias=True, exclude_none=exclude_none)  # type: ignore[attr-defined]
        return self.dict(by_alias=True, exclude_none=exclude_none)  # type: ignore[attr-defined]


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
