from __future__ import annotations

import pprint


class MarketInstrumentList(object):
    swagger_types: dict[str, str] = {
        'total': 'float',
        'instruments': 'list[MarketInstrument]'
    }

    attribute_map: dict[str, str] = {
        'total': 'total',
        'instruments': 'instruments'
    }

    def __init__(self, total=None, instruments=None):
        """MarketInstrumentList - a model defined in Swagger"""
        self._total = None
        self._instruments = None
        self.discriminator = None
        self.total = total
        self.instruments = instruments

    @property
    def total(self):
        """Gets the total of this MarketInstrumentList.

        :returns: The total of this MarketInstrumentList.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MarketInstrumentList.

        :param total: The total of this MarketInstrumentList.
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")

        self._total = total

    @property
    def instruments(self):
        """Gets the instruments of this MarketInstrumentList.

        :returns: The instruments of this MarketInstrumentList.
        :rtype: list[clients.tinkoff.models.MarketInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this MarketInstrumentList.

        :param instruments: The instruments of this MarketInstrumentList.
        :type: list[clients.tinkoff.models.MarketInstrument]
        """
        if instruments is None:
            raise ValueError("Invalid value for `instruments`, must not be `None`")

        self._instruments = instruments

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
        if not isinstance(other, MarketInstrumentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other