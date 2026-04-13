# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .search_result import SearchResult

__all__ = ["SearchResponse", "ClarificationNeeded"]


class ClarificationNeeded(BaseModel):
    """Present when status is `clarification_needed`."""

    options: Optional[List[str]] = None
    """Suggested answer options."""

    question: Optional[str] = None
    """The clarification question."""


class SearchResponse(BaseModel):
    results: List[SearchResult]

    session_id: str
    """Unique identifier for this search session."""

    status: Literal["completed", "clarification_needed", "failed"]

    synthesis: str
    """Synthesized summary of all findings."""

    clarification_needed: Optional[ClarificationNeeded] = None
    """Present when status is `clarification_needed`."""

    documents_scanned: Optional[int] = None
    """Number of documents scanned during the search."""

    queries_executed: Optional[int] = None
    """Number of queries executed during the search."""
