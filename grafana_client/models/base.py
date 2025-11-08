from typing import Any, Dict, Type, TypeVar

from pydantic import BaseModel, ConfigDict

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


__all__ = [
    "GrafanaBaseModel",
]
