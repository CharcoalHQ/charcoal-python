# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKeyCreateResponse", "APIKey"]


class APIKey(BaseModel):
    id: str
    """Unique API key identifier (e.g. `akey_CjXuYOtW`)."""

    created_at: datetime
    """ISO 8601 timestamp."""

    created_by: str
    """Name or identifier of the user who created the key."""

    key_prefix: str
    """The prefix portion of the key (e.g. `sk-prod`)."""

    key_suffix: str
    """The last few characters of the key, for display."""

    last_used_at: Optional[datetime] = None
    """
    ISO 8601 timestamp of the last request authenticated with this key, or `null` if
    never used.
    """

    name: str
    """Human-readable key name."""


class APIKeyCreateResponse(BaseModel):
    """Response from creating an API key.

    The `raw_key` field is only returned on creation and cannot be retrieved again — store it securely.
    """

    api_key: APIKey

    raw_key: str
    """The full API key. Only returned at creation time."""
