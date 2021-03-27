from __future__ import annotations

import pprint


class Candles(object):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'interval': 'CandleResolution',
        'candles': 'list[Candle]',
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'interval': 'interval',
        'candles': 'candles',
    }

    def __init__(self, figi=None, interval=None, candles=None):
        """Candles - a model defined in Swagger"""
        self._figi = None
        self._interval = None
        self._candles = None
        self.discriminator = None
        self.figi = figi
        self.interval = interval
        self.candles = candles

    @property
    def figi(self):
        """Gets the figi of this Candles.

        :returns: The figi of this Candles.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Candles.

        :param str figi: The figi of this Candles.
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def interval(self):
        """Gets the interval of this Candles.

        :returns: The interval of this Candles.
        :rtype: clients.tinkoff.models.CandleResolution
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Candles.

        :param clients.tinkoff.models.CandleResolution interval:
            The interval of this Candles.
        """
        if interval is None:
            raise ValueError(
                'Invalid value for `interval`, must not be `None`'
            )

        self._interval = interval

    @property
    def candles(self):
        """Gets the candles of this Candles.

        :returns: The candles of this Candles.
        :rtype: list[clients.tinkoff.models.Candle]
        """
        return self._candles

    @candles.setter
    def candles(self, candles):
        """Sets the candles of this Candles.

        :param list[clients.tinkoff.models.Candle] candles: The candles of this Candles.
        """
        if candles is None:
            raise ValueError('Invalid value for `candles`, must not be `None`')

        self._candles = candles

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
        if not isinstance(other, Candles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
