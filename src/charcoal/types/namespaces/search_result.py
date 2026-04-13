# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["SearchResult"]


class SearchResult(BaseModel):
    id: str
    """Source document ID."""

    excerpts: List[str]

    finding: str

    attributes: Optional[Dict[str, object]] = None
    """Document attributes. Present when `include_attributes` is `true`."""
