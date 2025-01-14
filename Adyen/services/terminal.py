from .base import AdyenServiceBase


class AdyenTerminalApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenTerminalApi, self).__init__(client=client)
        self.service = "terminal"

    def assign_terminals(self, request, idempotency_key=None, **kwargs):
        """
        Assign terminals
        """
        endpoint = f"/assignTerminals"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def find_terminal(self, request, idempotency_key=None, **kwargs):
        """
        Get the account or store of a terminal
        """
        endpoint = f"/findTerminal"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_stores_under_account(self, request, idempotency_key=None, **kwargs):
        """
        Get the stores of an account
        """
        endpoint = f"/getStoresUnderAccount"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terminal_details(self, request, idempotency_key=None, **kwargs):
        """
        Get the details of a terminal
        """
        endpoint = f"/getTerminalDetails"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terminals_under_account(self, request, idempotency_key=None, **kwargs):
        """
        Get the list of terminals
        """
        endpoint = f"/getTerminalsUnderAccount"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

