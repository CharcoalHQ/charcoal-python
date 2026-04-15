# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "SearchCreateParamsBase",
    "Filters",
    "FiltersAndCondition",
    "FiltersOrCondition",
    "FiltersFieldConditionFiltersFieldConditionItem",
    "FiltersFieldConditionFiltersFieldConditionItemEquals",
    "FiltersFieldConditionFiltersFieldConditionItemNotEquals",
    "FiltersFieldConditionFiltersFieldConditionItemGreaterThan",
    "FiltersFieldConditionFiltersFieldConditionItemGreaterThanOrEqual",
    "FiltersFieldConditionFiltersFieldConditionItemLessThan",
    "FiltersFieldConditionFiltersFieldConditionItemLessThanOrEqual",
    "FiltersFieldConditionFiltersFieldConditionItemIn",
    "FiltersFieldConditionFiltersFieldConditionItemNotIn",
    "FiltersFieldConditionFiltersFieldConditionItemContains",
    "FiltersFieldConditionFiltersFieldConditionItemContainsAny",
    "FiltersFieldConditionFiltersFieldConditionItemGlob",
    "FiltersFieldConditionFiltersFieldConditionItemCaseInsensitiveGlob",
    "SearchCreateParamsNonStreaming",
    "SearchCreateParamsStreaming",
]


class SearchCreateParamsBase(TypedDict, total=False):
    context: Required[str]
    """Additional context that helps the search system understand your intent.

    For example, relevant terminology, constraints, or prior knowledge.
    """

    objective: Required[str]
    """One sentence describing what you are looking for."""

    filters: Filters
    """Recursive filter object.

    One of: `{ $and: [Filter, ...] }` (all must match), `{ $or: [Filter, ...] }`
    (any must match), or `{ field_name: FieldCondition }` (field-level condition).
    """

    include_attributes: bool
    """Whether to include document attributes in search results."""

    multiturn: bool
    """Enable multi-turn mode.

    When `true`, the response includes a `session_id` and may return
    `clarification_needed` status. When `false` (default), the search always
    completes in a single request.
    """


class FiltersAndCondition(TypedDict, total=False):
    and_: Required[Annotated[Iterable[object], PropertyInfo(alias="$and")]]


class FiltersOrCondition(TypedDict, total=False):
    or_: Required[Annotated[Iterable[object], PropertyInfo(alias="$or")]]


class FiltersFieldConditionFiltersFieldConditionItemEquals(TypedDict, total=False):
    eq: Annotated[Union[str, float, bool, None], PropertyInfo(alias="$eq")]


class FiltersFieldConditionFiltersFieldConditionItemNotEquals(TypedDict, total=False):
    neq: Annotated[Union[str, float, bool, None], PropertyInfo(alias="$neq")]


class FiltersFieldConditionFiltersFieldConditionItemGreaterThan(TypedDict, total=False):
    gt: Annotated[float, PropertyInfo(alias="$gt")]


class FiltersFieldConditionFiltersFieldConditionItemGreaterThanOrEqual(TypedDict, total=False):
    gte: Annotated[float, PropertyInfo(alias="$gte")]


class FiltersFieldConditionFiltersFieldConditionItemLessThan(TypedDict, total=False):
    lt: Annotated[float, PropertyInfo(alias="$lt")]


class FiltersFieldConditionFiltersFieldConditionItemLessThanOrEqual(TypedDict, total=False):
    lte: Annotated[float, PropertyInfo(alias="$lte")]


class FiltersFieldConditionFiltersFieldConditionItemIn(TypedDict, total=False):
    in_: Annotated[SequenceNotStr[Union[str, float, bool, None]], PropertyInfo(alias="$in")]


class FiltersFieldConditionFiltersFieldConditionItemNotIn(TypedDict, total=False):
    not_in: Annotated[SequenceNotStr[Union[str, float, bool, None]], PropertyInfo(alias="$not_in")]


class FiltersFieldConditionFiltersFieldConditionItemContains(TypedDict, total=False):
    contains: Annotated[Union[str, float, bool, None], PropertyInfo(alias="$contains")]


class FiltersFieldConditionFiltersFieldConditionItemContainsAny(TypedDict, total=False):
    contains_any: Annotated[SequenceNotStr[Union[str, float, bool, None]], PropertyInfo(alias="$contains_any")]


class FiltersFieldConditionFiltersFieldConditionItemGlob(TypedDict, total=False):
    glob: Annotated[str, PropertyInfo(alias="$glob")]
    """Case-sensitive glob pattern match."""


class FiltersFieldConditionFiltersFieldConditionItemCaseInsensitiveGlob(TypedDict, total=False):
    iglob: Annotated[str, PropertyInfo(alias="$iglob")]
    """Case-insensitive glob pattern match."""


FiltersFieldConditionFiltersFieldConditionItem: TypeAlias = Union[
    str,
    float,
    bool,
    FiltersFieldConditionFiltersFieldConditionItemEquals,
    FiltersFieldConditionFiltersFieldConditionItemNotEquals,
    FiltersFieldConditionFiltersFieldConditionItemGreaterThan,
    FiltersFieldConditionFiltersFieldConditionItemGreaterThanOrEqual,
    FiltersFieldConditionFiltersFieldConditionItemLessThan,
    FiltersFieldConditionFiltersFieldConditionItemLessThanOrEqual,
    FiltersFieldConditionFiltersFieldConditionItemIn,
    FiltersFieldConditionFiltersFieldConditionItemNotIn,
    FiltersFieldConditionFiltersFieldConditionItemContains,
    FiltersFieldConditionFiltersFieldConditionItemContainsAny,
    FiltersFieldConditionFiltersFieldConditionItemGlob,
    FiltersFieldConditionFiltersFieldConditionItemCaseInsensitiveGlob,
]

Filters: TypeAlias = Union[
    FiltersAndCondition, FiltersOrCondition, Dict[str, FiltersFieldConditionFiltersFieldConditionItem]
]


class SearchCreateParamsNonStreaming(SearchCreateParamsBase, total=False):
    stream: Literal[False]
    """Whether to stream the response as server-sent events."""


class SearchCreateParamsStreaming(SearchCreateParamsBase):
    stream: Required[Literal[True]]
    """Whether to stream the response as server-sent events."""


SearchCreateParams = Union[SearchCreateParamsNonStreaming, SearchCreateParamsStreaming]
