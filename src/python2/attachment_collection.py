# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import attachment_request_builder # import AttachmentRequestBuilder
#from .attachment_request_builder import AttachmentRequestBuilder
from ..model.attachment import Attachment
import json

class AttachmentCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the AttachmentCollectionRequest
        
        Args:
            request_url (str): The url to perform the AttachmentCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(AttachmentCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the AttachmentCollectionPage

        Returns: 
            :class:`AttachmentCollectionPage<microsoft.msgraph.request.attachment_collection.AttachmentCollectionPage>`:
                The AttachmentCollectionPage
        """
        self.method = "GET"
        collection_response = AttachmentCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class AttachmentCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the AttachmentRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a AttachmentRequestBuilder for
        
        Returns: 
            :class:`AttachmentRequestBuilder<microsoft.msgraph.request.attachment_request_builder.AttachmentRequestBuilder>`:
                A AttachmentRequestBuilder for that key
        """
        return attachment_request_builder.AttachmentRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the AttachmentCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`AttachmentCollectionRequest<microsoft.msgraph.request.attachment_collection.AttachmentCollectionRequest>`:
                The AttachmentCollectionRequest
        """
        req = AttachmentCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the AttachmentCollectionPage

        Returns: 
            :class:`AttachmentCollectionPage<microsoft.msgraph.request.attachment_collection.AttachmentCollectionPage>`:
                The AttachmentCollectionPage
        """
        return self.request().get()



class AttachmentCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`AttachmentCollectionPage<microsoft.msgraph.request.attachment_collection.AttachmentCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = AttachmentCollectionPage(self._prop_dict["value"])

        return self._collection_page


class AttachmentCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Attachment at the index specified
        
        Args:
            index (int): The index of the item to get from the AttachmentCollectionPage

        Returns:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The Attachment at the index
        """
        return Attachment(self._prop_list[index])

    def attachment(self):
        """Get a generator of Attachment within the AttachmentCollectionPage
        
        Yields:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The next Attachment in the collection
        """
        for item in self._prop_list:
            yield Attachment(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the AttachmentCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = AttachmentCollectionRequest(next_page_link, client, options)
