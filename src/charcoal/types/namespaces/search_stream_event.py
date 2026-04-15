# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .search_response import SearchResponse

__all__ = ["SearchStreamEvent", "SearchStatusEvent", "SearchSessionResultEvent", "SearchErrorEvent"]


class SearchStatusEvent(BaseModel):
    """Progress update emitted while a search is running."""

    message: str
    """Human-readable progress message."""

    type: Literal["status"]


class SearchSessionResultEvent(SearchResponse):
    """Final search result.

    Carries the same fields as `SearchResponse` plus a `type` discriminator.
    """

    type: Literal["session_result"]


class SearchErrorEvent(BaseModel):
    """Emitted when a streaming search fails."""

    code: str
    """Stable error code describing the failure."""

    type: Literal["error"]


SearchStreamEvent: TypeAlias = Annotated[
    Union[SearchStatusEvent, SearchSessionResultEvent, SearchErrorEvent], PropertyInfo(discriminator="type")
]
