# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .api_key import APIKey
from .._models import BaseModel

__all__ = ["CreateAPIKeyResponse"]


class CreateAPIKeyResponse(BaseModel):
    """Response from creating an API key.

    The `raw_key` field is only returned on creation and cannot be retrieved again — store it securely.
    """

    api_key: APIKey

    raw_key: str
    """The full API key. Only returned at creation time."""
