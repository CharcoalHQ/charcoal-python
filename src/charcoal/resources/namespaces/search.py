# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.namespaces import search_create_params, search_continue_params
from ...types.namespaces.search_response import SearchResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """Agentic search over document corpora."""

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        namespace: str,
        *,
        context: str,
        objective: str,
        filters: search_create_params.Filters | Omit = omit,
        include_attributes: bool | Omit = omit,
        multiturn: bool | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches the documents in a namespace.

        Set `multiturn: true` to enable multi-turn mode, which returns a `session_id`
        and may return `clarification_needed` status when the system needs more
        information.

        ### Streaming

        Set `stream: true` to receive results as server-sent events. The stream emits
        three event types:

        - **`status`** — Progress updates during search. Payload:
          `{ "message": "string" }`
        - **`session_result`** — The final search result. Payload matches the
          non-streaming response schema.
        - **`error`** — Sent if the search fails. Payload: `{ "code": "string" }`

        The stream closes after either a `session_result` or `error` event.

        Args:
          context: Additional context that helps the search system understand your intent. For
              example, relevant terminology, constraints, or prior knowledge.

          objective: One sentence describing what you are looking for.

          filters: Recursive filter object. One of: `{ $and: [Filter, ...] }` (all must match),
              `{ $or: [Filter, ...] }` (any must match), or `{ field_name: FieldCondition }`
              (field-level condition).

          include_attributes: Whether to include document attributes in search results.

          multiturn: Enable multi-turn mode. When `true`, the response includes a `session_id` and
              may return `clarification_needed` status. When `false` (default), the search
              always completes in a single request.

          stream: Whether to stream the response as server-sent events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._post(
            path_template("/v1/namespaces/{namespace}/search", namespace=namespace),
            body=maybe_transform(
                {
                    "context": context,
                    "objective": objective,
                    "filters": filters,
                    "include_attributes": include_attributes,
                    "multiturn": multiturn,
                    "stream": stream,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    def continue_(
        self,
        session_id: str,
        *,
        namespace: str,
        message: str,
        include_attributes: bool | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """Continues a multi-turn search session.

        Use this to respond to clarification
        questions or provide follow-up messages.

        ### Streaming

        Supports the same `stream` parameter and SSE event types as the search endpoint.

        Args:
          message: Follow-up message or answer to a clarification question.

          include_attributes: Whether to include document attributes in search results.

          stream: Whether to stream the response as server-sent events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/v1/namespaces/{namespace}/search/{session_id}", namespace=namespace, session_id=session_id),
            body=maybe_transform(
                {
                    "message": message,
                    "include_attributes": include_attributes,
                    "stream": stream,
                },
                search_continue_params.SearchContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    """Agentic search over document corpora."""

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        namespace: str,
        *,
        context: str,
        objective: str,
        filters: search_create_params.Filters | Omit = omit,
        include_attributes: bool | Omit = omit,
        multiturn: bool | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches the documents in a namespace.

        Set `multiturn: true` to enable multi-turn mode, which returns a `session_id`
        and may return `clarification_needed` status when the system needs more
        information.

        ### Streaming

        Set `stream: true` to receive results as server-sent events. The stream emits
        three event types:

        - **`status`** — Progress updates during search. Payload:
          `{ "message": "string" }`
        - **`session_result`** — The final search result. Payload matches the
          non-streaming response schema.
        - **`error`** — Sent if the search fails. Payload: `{ "code": "string" }`

        The stream closes after either a `session_result` or `error` event.

        Args:
          context: Additional context that helps the search system understand your intent. For
              example, relevant terminology, constraints, or prior knowledge.

          objective: One sentence describing what you are looking for.

          filters: Recursive filter object. One of: `{ $and: [Filter, ...] }` (all must match),
              `{ $or: [Filter, ...] }` (any must match), or `{ field_name: FieldCondition }`
              (field-level condition).

          include_attributes: Whether to include document attributes in search results.

          multiturn: Enable multi-turn mode. When `true`, the response includes a `session_id` and
              may return `clarification_needed` status. When `false` (default), the search
              always completes in a single request.

          stream: Whether to stream the response as server-sent events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._post(
            path_template("/v1/namespaces/{namespace}/search", namespace=namespace),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "objective": objective,
                    "filters": filters,
                    "include_attributes": include_attributes,
                    "multiturn": multiturn,
                    "stream": stream,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    async def continue_(
        self,
        session_id: str,
        *,
        namespace: str,
        message: str,
        include_attributes: bool | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """Continues a multi-turn search session.

        Use this to respond to clarification
        questions or provide follow-up messages.

        ### Streaming

        Supports the same `stream` parameter and SSE event types as the search endpoint.

        Args:
          message: Follow-up message or answer to a clarification question.

          include_attributes: Whether to include document attributes in search results.

          stream: Whether to stream the response as server-sent events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/v1/namespaces/{namespace}/search/{session_id}", namespace=namespace, session_id=session_id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "include_attributes": include_attributes,
                    "stream": stream,
                },
                search_continue_params.SearchContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )
        self.continue_ = to_raw_response_wrapper(
            search.continue_,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )
        self.continue_ = async_to_raw_response_wrapper(
            search.continue_,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )
        self.continue_ = to_streamed_response_wrapper(
            search.continue_,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
        self.continue_ = async_to_streamed_response_wrapper(
            search.continue_,
        )
