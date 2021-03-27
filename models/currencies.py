from __future__ import annotations

import pprint


class Currencies(object):
    swagger_types: dict[str, str] = {'currencies': 'list[CurrencyPosition]'}

    attribute_map: dict[str, str] = {'currencies': 'currencies'}

    def __init__(self, currencies=None):
        """Currencies - a model defined in Swagger"""
        self._currencies = None
        self.discriminator = None
        self.currencies = currencies

    @property
    def currencies(self):
        """Gets the currencies of this Currencies.

        :returns: The currencies of this Currencies.
        :rtype: list[clients.tinkoff.models.CurrencyPosition]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this Currencies.

        :param currencies: The currencies of this Currencies.
        :type: list[clients.tinkoff.models.CurrencyPosition]
        """
        if currencies is None:
            raise ValueError(
                'Invalid value for `currencies`, must not be `None`'
            )

        self._currencies = currencies

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
        if not isinstance(other, Currencies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
