from __future__ import annotations

import pprint


class SandboxSetCurrencyBalanceRequest(object):
    swagger_types: dict[str, str] = {
        'currency': 'SandboxCurrency',
        'balance': 'float'
    }

    attribute_map: dict[str, str] = {
        'currency': 'currency',
        'balance': 'balance'
    }

    def __init__(self, currency=None, balance=None):
        """SandboxSetCurrencyBalanceRequest - a model defined in Swagger"""
        self._currency = None
        self._balance = None
        self.discriminator = None
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        """Gets the currency of this SandboxSetCurrencyBalanceRequest.

        :returns: The currency of this SandboxSetCurrencyBalanceRequest.
        :rtype: clients.tinkoff.models.SandboxCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SandboxSetCurrencyBalanceRequest.

        :param currency: The currency of this SandboxSetCurrencyBalanceRequest.
        :type currency: clients.tinkoff.models.SandboxCurrency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency

    @property
    def balance(self):
        """Gets the balance of this SandboxSetCurrencyBalanceRequest.

        :returns: The balance of this SandboxSetCurrencyBalanceRequest.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SandboxSetCurrencyBalanceRequest.

        :param balance: The balance of this SandboxSetCurrencyBalanceRequest.
        :type: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")

        self._balance = balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SandboxSetCurrencyBalanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
