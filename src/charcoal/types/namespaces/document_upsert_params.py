# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .document_param import DocumentParam

__all__ = ["DocumentUpsertParams", "Schema"]


class DocumentUpsertParams(TypedDict, total=False):
    documents: Required[Iterable[DocumentParam]]

    schema: Dict[str, Schema]
    """Explicit schema for the documents.

    If omitted, schema is inferred from the document structure and merged with any
    existing namespace schema.
    """


class Schema(TypedDict, total=False):
    type: Required[
        Literal[
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
    ]

    is_filterable: bool
    """Whether this attribute can be filtered on."""

    is_searchable: bool
    """Whether this attribute can be searched against."""
