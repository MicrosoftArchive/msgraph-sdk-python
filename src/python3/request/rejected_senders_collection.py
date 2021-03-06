# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import directory_object_request_builder 
from ..model.directory_object import DirectoryObject
import json
import asyncio

class RejectedSendersCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the RejectedSendersCollectionRequest
        
        Args:
            request_url (str): The url to perform the RejectedSendersCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(RejectedSendersCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the RejectedSendersCollectionPage

        Returns: 
            :class:`RejectedSendersCollectionPage<msgraph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The RejectedSendersCollectionPage
        """
        self.method = "GET"
        collection_response = RejectedSendersCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the RejectedSendersCollectionPage in async

        Yields: 
            :class:`RejectedSendersCollectionPage<msgraph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The RejectedSendersCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class RejectedSendersCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DirectoryObjectRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DirectoryObjectRequestBuilder for
        
        Returns: 
            :class:`DirectoryObjectRequestBuilder<msgraph.request.directory_object_request_builder.DirectoryObjectRequestBuilder>`:
                A DirectoryObjectRequestBuilder for that key
        """
        return directory_object_request_builder.DirectoryObjectRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,top=None, order_by=None, options=None):
        """Builds the RejectedSendersCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`RejectedSendersCollectionRequest<msgraph.request.rejected_senders_collection.RejectedSendersCollectionRequest>`:
                The RejectedSendersCollectionRequest
        """
        req = RejectedSendersCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(top=top, order_by=order_by, )
        return req

    def get(self):
        """Gets the RejectedSendersCollectionPage

        Returns: 
            :class:`RejectedSendersCollectionPage<msgraph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The RejectedSendersCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the RejectedSendersCollectionPage in async

        Yields: 
            :class:`RejectedSendersCollectionPage<msgraph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The RejectedSendersCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class RejectedSendersCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`RejectedSendersCollectionPage<msgraph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = RejectedSendersCollectionPage(self._prop_dict["value"])

        return self._collection_page


class RejectedSendersCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the DirectoryObject at the index specified
        
        Args:
            index (int): The index of the item to get from the RejectedSendersCollectionPage

        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject at the index
        """
        return DirectoryObject(self._prop_list[index])

    def rejected_senders(self):
        """Get a generator of DirectoryObject within the RejectedSendersCollectionPage
        
        Yields:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The next DirectoryObject in the collection
        """
        for item in self._prop_list:
            yield DirectoryObject(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the RejectedSendersCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = RejectedSendersCollectionRequest(next_page_link, client, options)
