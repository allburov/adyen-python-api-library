"""
    Adyen Payout API

    A set of API endpoints that allow you to store payout details, confirm, or decline a payout.  For more information, refer to [Online payouts](https://docs.adyen.com/online-payments/online-payouts). ## Authentication To use the Payout API, you need to have [two API credentials](https://docs.adyen.com/online-payments/online-payouts#payouts-to-bank-accounts-and-wallets): one for storing payout details and submitting payouts, and another one for confirming or declining payouts. If you don't have the required API credentials, contact our [Support Team](https://www.adyen.help/hc/en-us/requests/new).  Both of these API credentials must be authenticated with [basic authentication](https://docs.adyen.com/development-resources/api-credentials#basic-authentication).The following example shows how to authenticate your request when submitting a payout:  ``` curl -U \"storePayout@Company.YOUR_COMPANY_ACCOUNT\":\"YOUR_BASIC_AUTHENTICATION_PASSWORD\" \\ -H \"Content-Type: application/json\" \\ ... ```  ## Versioning Payments API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.  For example: ``` https://pal-test.adyen.com/pal/servlet/Payout/v68/payout ```  ## Going live  To authenticate to the live endpoints, you need [API credentials](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.  The live endpoint URLs contain a prefix which is unique to your company account: ```  https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payout/v68/payout ```  Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**.  # noqa: E501

    The version of the OpenAPI document: 68
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""

from ..base import AdyenServiceBase
from .initialization_api import InitializationApi
from .instant_payouts_api import InstantPayoutsApi
from .reviewing_api import ReviewingApi


class AdyenPayoutsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenPayoutsApi, self).__init__(client=client)
        self.initialization_api = InitializationApi(client=client)
        self.instant_payouts_api = InstantPayoutsApi(client=client)
        self.reviewing_api = ReviewingApi(client=client)