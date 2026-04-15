# Namespaces

Types:

```python
from charcoal.types import Namespace, NamespaceListResponse
```

Methods:

- <code title="get /v1/namespaces">client.namespaces.<a href="./src/charcoal/resources/namespaces/namespaces.py">list</a>() -> <a href="./src/charcoal/types/namespace_list_response.py">NamespaceListResponse</a></code>

## Documents

Types:

```python
from charcoal.types.namespaces import DeleteDocumentsResponse, Document, UpsertDocumentsResponse
```

Methods:

- <code title="get /v1/namespaces/{namespace}/documents/{documentId}">client.namespaces.documents.<a href="./src/charcoal/resources/namespaces/documents.py">retrieve</a>(document_id, \*, namespace) -> <a href="./src/charcoal/types/namespaces/document.py">Document</a></code>
- <code title="post /v1/namespaces/{namespace}/documents/delete">client.namespaces.documents.<a href="./src/charcoal/resources/namespaces/documents.py">delete</a>(namespace, \*\*<a href="src/charcoal/types/namespaces/document_delete_params.py">params</a>) -> <a href="./src/charcoal/types/namespaces/delete_documents_response.py">DeleteDocumentsResponse</a></code>
- <code title="post /v1/namespaces/{namespace}/documents">client.namespaces.documents.<a href="./src/charcoal/resources/namespaces/documents.py">upsert</a>(namespace, \*\*<a href="src/charcoal/types/namespaces/document_upsert_params.py">params</a>) -> <a href="./src/charcoal/types/namespaces/upsert_documents_response.py">UpsertDocumentsResponse</a></code>

## Search

Types:

```python
from charcoal.types.namespaces import (
    SearchContinuationRequest,
    SearchRequest,
    SearchResponse,
    SearchResult,
    SearchStreamEvent,
)
```

Methods:

- <code title="post /v1/namespaces/{namespace}/search">client.namespaces.search.<a href="./src/charcoal/resources/namespaces/search.py">create</a>(namespace, \*\*<a href="src/charcoal/types/namespaces/search_create_params.py">params</a>) -> <a href="./src/charcoal/types/namespaces/search_response.py">SearchResponse</a></code>
- <code title="post /v1/namespaces/{namespace}/search/{session_id}">client.namespaces.search.<a href="./src/charcoal/resources/namespaces/search.py">continue\_</a>(session_id, \*, namespace, \*\*<a href="src/charcoal/types/namespaces/search_continue_params.py">params</a>) -> <a href="./src/charcoal/types/namespaces/search_response.py">SearchResponse</a></code>

# APIKeys

Types:

```python
from charcoal.types import APIKey, CreateAPIKeyResponse, APIKeyListResponse, APIKeyDeleteResponse
```

Methods:

- <code title="post /v1/api_keys">client.api_keys.<a href="./src/charcoal/resources/api_keys.py">create</a>(\*\*<a href="src/charcoal/types/api_key_create_params.py">params</a>) -> <a href="./src/charcoal/types/create_api_key_response.py">CreateAPIKeyResponse</a></code>
- <code title="get /v1/api_keys">client.api_keys.<a href="./src/charcoal/resources/api_keys.py">list</a>() -> <a href="./src/charcoal/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v1/api_keys/{id}">client.api_keys.<a href="./src/charcoal/resources/api_keys.py">delete</a>(id) -> <a href="./src/charcoal/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
