# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.namespace_list_response import NamespaceListResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    """Manage namespaces."""

    @cached_property
    def documents(self) -> DocumentsResource:
        """Manage documents within namespaces."""
        return DocumentsResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        """Agentic search over document corpora."""
        return SearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#accessing-raw-response-data-eg-headers
        """
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#with_streaming_response
        """
        return NamespacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """Lists all namespaces for the authenticated organization."""
        return self._get(
            "/v1/namespaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceListResponse,
        )


class AsyncNamespacesResource(AsyncAPIResource):
    """Manage namespaces."""

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        """Manage documents within namespaces."""
        return AsyncDocumentsResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """Agentic search over document corpora."""
        return AsyncSearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CharcoalHQ/charcoal-python#with_streaming_response
        """
        return AsyncNamespacesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """Lists all namespaces for the authenticated organization."""
        return await self._get(
            "/v1/namespaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceListResponse,
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        """Manage documents within namespaces."""
        return DocumentsResourceWithRawResponse(self._namespaces.documents)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        """Agentic search over document corpora."""
        return SearchResourceWithRawResponse(self._namespaces.search)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        """Manage documents within namespaces."""
        return AsyncDocumentsResourceWithRawResponse(self._namespaces.documents)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        """Agentic search over document corpora."""
        return AsyncSearchResourceWithRawResponse(self._namespaces.search)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        """Manage documents within namespaces."""
        return DocumentsResourceWithStreamingResponse(self._namespaces.documents)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        """Agentic search over document corpora."""
        return SearchResourceWithStreamingResponse(self._namespaces.search)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """Manage documents within namespaces."""
        return AsyncDocumentsResourceWithStreamingResponse(self._namespaces.documents)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        """Agentic search over document corpora."""
        return AsyncSearchResourceWithStreamingResponse(self._namespaces.search)
