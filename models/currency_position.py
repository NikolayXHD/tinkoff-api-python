from __future__ import annotations

import pprint


class CurrencyPosition(object):
    swagger_types: dict[str, str] = {
        'currency': 'Currency',
        'balance': 'float',
        'blocked': 'float',
    }

    attribute_map: dict[str, str] = {
        'currency': 'currency',
        'balance': 'balance',
        'blocked': 'blocked',
    }

    def __init__(self, currency=None, balance=None, blocked=None):
        """CurrencyPosition - a model defined in Swagger"""
        self._currency = None
        self._balance = None
        self._blocked = None
        self.discriminator = None
        self.currency = currency
        self.balance = balance
        if blocked is not None:
            self.blocked = blocked

    @property
    def currency(self):
        """Gets the currency of this CurrencyPosition.

        :returns: The currency of this CurrencyPosition.
                  clients.tinkoff.models.Currency
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CurrencyPosition.

        :param clients.tinkoff.models.Currency currency:
            The currency of this CurrencyPosition.
        """
        if currency is None:
            raise ValueError(
                'Invalid value for `currency`, must not be `None`'
            )

        self._currency = currency

    @property
    def balance(self):
        """Gets the balance of this CurrencyPosition.

        :returns: The balance of this CurrencyPosition.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CurrencyPosition.

        :param balance: The balance of this CurrencyPosition.
        :type: float
        """
        if balance is None:
            raise ValueError('Invalid value for `balance`, must not be `None`')

        self._balance = balance

    @property
    def blocked(self):
        """Gets the blocked of this CurrencyPosition.

        :returns: The blocked of this CurrencyPosition.
        :rtype: float
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this CurrencyPosition.

        :param blocked: The blocked of this CurrencyPosition.
        :type: float
        """

        self._blocked = blocked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(
                        lambda x: x.to_dict() if hasattr(x, 'to_dict') else x,
                        value,
                    )
                )
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict')
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, CurrencyPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
