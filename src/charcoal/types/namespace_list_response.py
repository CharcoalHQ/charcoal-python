# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .namespace import Namespace

__all__ = ["NamespaceListResponse"]


class NamespaceListResponse(BaseModel):
    results: List[Namespace]
