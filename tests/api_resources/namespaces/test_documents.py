# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from charcoal import Charcoal, AsyncCharcoal
from tests.utils import assert_matches_type
from charcoal.types.namespaces import (
    Document,
    DeleteDocumentsResponse,
    UpsertDocumentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Charcoal) -> None:
        document = client.namespaces.documents.retrieve(
            document_id="documentId",
            namespace="namespace",
        )
        assert_matches_type(Document, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Charcoal) -> None:
        response = client.namespaces.documents.with_raw_response.retrieve(
            document_id="documentId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Charcoal) -> None:
        with client.namespaces.documents.with_streaming_response.retrieve(
            document_id="documentId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Charcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.namespaces.documents.with_raw_response.retrieve(
                document_id="documentId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.namespaces.documents.with_raw_response.retrieve(
                document_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Charcoal) -> None:
        document = client.namespaces.documents.delete(
            namespace="namespace",
            document_ids=["string"],
        )
        assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Charcoal) -> None:
        response = client.namespaces.documents.with_raw_response.delete(
            namespace="namespace",
            document_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Charcoal) -> None:
        with client.namespaces.documents.with_streaming_response.delete(
            namespace="namespace",
            document_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Charcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.namespaces.documents.with_raw_response.delete(
                namespace="",
                document_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Charcoal) -> None:
        document = client.namespaces.documents.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        )
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Charcoal) -> None:
        document = client.namespaces.documents.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
            schema={
                "foo": {
                    "type": "string",
                    "is_filterable": True,
                    "is_searchable": True,
                }
            },
        )
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Charcoal) -> None:
        response = client.namespaces.documents.with_raw_response.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Charcoal) -> None:
        with client.namespaces.documents.with_streaming_response.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Charcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.namespaces.documents.with_raw_response.upsert(
                namespace="",
                documents=[{"id": "id"}],
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCharcoal) -> None:
        document = await async_client.namespaces.documents.retrieve(
            document_id="documentId",
            namespace="namespace",
        )
        assert_matches_type(Document, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCharcoal) -> None:
        response = await async_client.namespaces.documents.with_raw_response.retrieve(
            document_id="documentId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCharcoal) -> None:
        async with async_client.namespaces.documents.with_streaming_response.retrieve(
            document_id="documentId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCharcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.namespaces.documents.with_raw_response.retrieve(
                document_id="documentId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.namespaces.documents.with_raw_response.retrieve(
                document_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCharcoal) -> None:
        document = await async_client.namespaces.documents.delete(
            namespace="namespace",
            document_ids=["string"],
        )
        assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCharcoal) -> None:
        response = await async_client.namespaces.documents.with_raw_response.delete(
            namespace="namespace",
            document_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCharcoal) -> None:
        async with async_client.namespaces.documents.with_streaming_response.delete(
            namespace="namespace",
            document_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DeleteDocumentsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCharcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.namespaces.documents.with_raw_response.delete(
                namespace="",
                document_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncCharcoal) -> None:
        document = await async_client.namespaces.documents.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        )
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncCharcoal) -> None:
        document = await async_client.namespaces.documents.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
            schema={
                "foo": {
                    "type": "string",
                    "is_filterable": True,
                    "is_searchable": True,
                }
            },
        )
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncCharcoal) -> None:
        response = await async_client.namespaces.documents.with_raw_response.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncCharcoal) -> None:
        async with async_client.namespaces.documents.with_streaming_response.upsert(
            namespace="namespace",
            documents=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(UpsertDocumentsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncCharcoal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.namespaces.documents.with_raw_response.upsert(
                namespace="",
                documents=[{"id": "id"}],
            )
