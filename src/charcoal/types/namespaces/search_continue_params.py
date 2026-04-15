# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchContinueParamsBase", "SearchContinueParamsNonStreaming", "SearchContinueParamsStreaming"]


class SearchContinueParamsBase(TypedDict, total=False):
    namespace: Required[str]

    message: Required[str]
    """Follow-up message or answer to a clarification question."""

    include_attributes: bool
    """Whether to include document attributes in search results."""


class SearchContinueParamsNonStreaming(SearchContinueParamsBase, total=False):
    stream: Literal[False]
    """Whether to stream the response as server-sent events."""


class SearchContinueParamsStreaming(SearchContinueParamsBase):
    stream: Required[Literal[True]]
    """Whether to stream the response as server-sent events."""


SearchContinueParams = Union[SearchContinueParamsNonStreaming, SearchContinueParamsStreaming]
