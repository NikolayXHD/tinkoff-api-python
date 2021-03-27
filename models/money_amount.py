from __future__ import annotations

import pprint


class MoneyAmount(object):
    swagger_types: dict[str, str] = {'currency': 'Currency', 'value': 'float'}

    attribute_map: dict[str, str] = {'currency': 'currency', 'value': 'value'}

    def __init__(self, currency=None, value=None):
        """MoneyAmount - a model defined in Swagger"""
        self._currency = None
        self._value = None
        self.discriminator = None
        self.currency = currency
        self.value = value

    @property
    def currency(self):
        """Gets the currency of this MoneyAmount.

        :returns: The currency of this MoneyAmount.
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MoneyAmount.

        :param clients.tinkoff.models.Currency currency:
            The currency of this MoneyAmount.
        """
        if currency is None:
            raise ValueError(
                'Invalid value for `currency`, must not be `None`'
            )

        self._currency = currency

    @property
    def value(self):
        """Gets the value of this MoneyAmount.

        :returns: The value of this MoneyAmount.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MoneyAmount.

        :param float value: The value of this MoneyAmount.
        """
        if value is None:
            raise ValueError('Invalid value for `value`, must not be `None`')

        self._value = value

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
        if not isinstance(other, MoneyAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
