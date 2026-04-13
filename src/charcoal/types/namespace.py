# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Namespace", "AttributesSchema"]


class AttributesSchema(BaseModel):
    type: Literal[
        "string",
        "int",
        "uint",
        "float",
        "uuid",
        "datetime",
        "bool",
        "[]string",
        "[]int",
        "[]uint",
        "[]float",
        "[]uuid",
        "[]datetime",
        "[]bool",
    ]

    is_filterable: Optional[bool] = None
    """Whether this attribute can be filtered on."""

    is_searchable: Optional[bool] = None
    """Whether this attribute can be searched against."""


class Namespace(BaseModel):
    id: str
    """Unique namespace identifier (e.g. `ns_CjXuYOtW`)."""

    created_at: datetime
    """ISO 8601 timestamp."""

    name: str
    """Namespace name. This is the value used in API path parameters."""

    updated_at: datetime
    """ISO 8601 timestamp."""

    attributes_schema: Optional[Dict[str, AttributesSchema]] = None
    """Maps attribute names to their configuration."""
