from ..base import AdyenServiceBase


class AccountStoreLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AccountStoreLevelApi, self).__init__(client=client)
        self.service = "management"

    def list_stores_by_merchant_id(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get a list of stores
        """
        endpoint = f"/merchants/{merchantId}/stores"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_store(self, merchantId, storeId, idempotency_key=None, **kwargs):
        """
        Get a store
        """
        endpoint = f"/merchants/{merchantId}/stores/{storeId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_stores(self, idempotency_key=None, **kwargs):
        """
        Get a list of stores
        """
        endpoint = f"/stores"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_store_by_id(self, storeId, idempotency_key=None, **kwargs):
        """
        Get a store
        """
        endpoint = f"/stores/{storeId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_store(self, request, merchantId, storeId, idempotency_key=None, **kwargs):
        """
        Update a store
        """
        endpoint = f"/merchants/{merchantId}/stores/{storeId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_store_by_id(self, request, storeId, idempotency_key=None, **kwargs):
        """
        Update a store
        """
        endpoint = f"/stores/{storeId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_store_by_merchant_id(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Create a store
        """
        endpoint = f"/merchants/{merchantId}/stores"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_store(self, request, idempotency_key=None, **kwargs):
        """
        Create a store
        """
        endpoint = f"/stores"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

