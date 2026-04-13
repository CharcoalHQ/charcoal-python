# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentParam"]


class DocumentParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A document is a record with a required `id` and arbitrary attributes.

    Attribute types must conform to the namespace's `attributes_schema`. If no schema is provided during upsert, one is inferred from the document structure.
    """

    id: Required[str]
    """Document ID. UUID or string up to 64 characters."""
