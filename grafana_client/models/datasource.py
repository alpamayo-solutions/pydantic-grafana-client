import dataclasses
from typing import Any, Dict, List, Optional, Union

from .base import GrafanaBaseModel


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

    TODO: Field ``database`` will be deprecated.
          https://github.com/grafana/grafana/issues/59115
    """

    name: str
    type: str
    url: str
    access: str
    database: Optional[str] = None
    user: Optional[str] = None
    jsonData: Optional[Dict[str, Any]] = None
    secureJsonData: Optional[Dict[str, Any]] = None
    secureJsonFields: Optional[Dict[str, Any]] = None

    def asdict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class DatasourceHealthResponse:
    """
    Represent a response for a Grafana data source health check.

    It is a mixture of the fields of the native, server-side health check
    introduced with Grafana 9+, and the client-side implementation by
    ``grafana-client``.

    - Grafana 9+ uses the fields ``status`` and ``message``, where ``status`` can be
      one of ``OK`` or ``ERROR``.
    - ``grafana-client`` employs a more verbose response, including metadata
      about the requested data source item (``uid``, ``type``), a boolean ``success``
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


__all__ = [
    "DatasourceIdentifier",
    "DatasourceModel",
    "DatasourceHealthResponse",
    "DatasourceUpsertModel",
    "DatasourcePermissionsModel",
    "DatasourcePermissionUpdateModel",
]


class DatasourceUpsertModel(GrafanaBaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None
    access: Optional[str] = None
    database: Optional[str] = None
    user: Optional[str] = None
    jsonData: Optional[Dict[str, Any]] = None
    secureJsonData: Optional[Dict[str, Any]] = None
    secureJsonFields: Optional[Dict[str, Any]] = None
    basicAuth: Optional[bool] = None
    basicAuthUser: Optional[str] = None
    basicAuthPassword: Optional[str] = None
    isDefault: Optional[bool] = None
    withCredentials: Optional[bool] = None
    orgId: Optional[int] = None
    uid: Optional[str] = None


class DatasourcePermissionsModel(GrafanaBaseModel):
    items: Optional[List[Dict[str, Any]]] = None


class DatasourcePermissionUpdateModel(GrafanaBaseModel):
    permission: Optional[Union[int, str]] = None
