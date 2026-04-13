# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from charcoal import Charcoal, AsyncCharcoal
from tests.utils import assert_matches_type
from charcoal.types.namespaces import SearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Charcoal) -> None:
        search = client.namespaces.search.create(
            namespace="namespace",
            context="context",
            objective="objective",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Charcoal) -> None:
        search = client.namespaces.search.create(
            namespace="namespace",
            context="context",
            objective="objective",
            filters={"and_": [{}]},
            include_attributes=True,
            multiturn=True,
            stream=True,
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Charcoal) -> None:
        response = client.namespaces.search.with_raw_response.create(
            namespace="namespace",
            context="context",
            objective="objective",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Charcoal) -> None:
        with client.namespaces.search.with_streaming_response.create(
            namespace="namespace",
            context="context",
            objective="objective",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Charcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.namespaces.search.with_raw_response.create(
                namespace="",
                context="context",
                objective="objective",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue(self, client: Charcoal) -> None:
        search = client.namespaces.search.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue_with_all_params(self, client: Charcoal) -> None:
        search = client.namespaces.search.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
            include_attributes=True,
            stream=True,
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_continue(self, client: Charcoal) -> None:
        response = client.namespaces.search.with_raw_response.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_continue(self, client: Charcoal) -> None:
        with client.namespaces.search.with_streaming_response.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_continue(self, client: Charcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.namespaces.search.with_raw_response.continue_(
                session_id="session_id",
                namespace="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.namespaces.search.with_raw_response.continue_(
                session_id="",
                namespace="namespace",
                message="message",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCharcoal) -> None:
        search = await async_client.namespaces.search.create(
            namespace="namespace",
            context="context",
            objective="objective",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCharcoal) -> None:
        search = await async_client.namespaces.search.create(
            namespace="namespace",
            context="context",
            objective="objective",
            filters={"and_": [{}]},
            include_attributes=True,
            multiturn=True,
            stream=True,
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCharcoal) -> None:
        response = await async_client.namespaces.search.with_raw_response.create(
            namespace="namespace",
            context="context",
            objective="objective",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCharcoal) -> None:
        async with async_client.namespaces.search.with_streaming_response.create(
            namespace="namespace",
            context="context",
            objective="objective",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCharcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.namespaces.search.with_raw_response.create(
                namespace="",
                context="context",
                objective="objective",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue(self, async_client: AsyncCharcoal) -> None:
        search = await async_client.namespaces.search.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue_with_all_params(self, async_client: AsyncCharcoal) -> None:
        search = await async_client.namespaces.search.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
            include_attributes=True,
            stream=True,
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_continue(self, async_client: AsyncCharcoal) -> None:
        response = await async_client.namespaces.search.with_raw_response.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_continue(self, async_client: AsyncCharcoal) -> None:
        async with async_client.namespaces.search.with_streaming_response.continue_(
            session_id="session_id",
            namespace="namespace",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_continue(self, async_client: AsyncCharcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.namespaces.search.with_raw_response.continue_(
                session_id="session_id",
                namespace="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.namespaces.search.with_raw_response.continue_(
                session_id="",
                namespace="namespace",
                message="message",
            )
