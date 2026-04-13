# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchContinueParams"]


class SearchContinueParams(TypedDict, total=False):
    namespace: Required[str]

    message: Required[str]
    """Follow-up message or answer to a clarification question."""

    include_attributes: bool
    """Whether to include document attributes in search results."""

    stream: bool
    """Whether to stream the response as server-sent events."""
