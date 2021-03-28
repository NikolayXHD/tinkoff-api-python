from __future__ import annotations

from . import _base


class Candles(_base.Model):
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
        self._figi = None
        self._interval = None
        self._candles = None
        self.discriminator = None
        self.figi = figi
        self.interval = interval
        self.candles = candles

    @property
    def figi(self):
        """
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """
        :param str figi:
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def interval(self):
        """
        :rtype: clients.tinkoff.models.CandleResolution
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        :param clients.tinkoff.models.CandleResolution interval:
        """
        if interval is None:
            raise ValueError(
                'Invalid value for `interval`, must not be `None`'
            )

        self._interval = interval

    @property
    def candles(self):
        """
        :rtype: list[clients.tinkoff.models.Candle]
        """
        return self._candles

    @candles.setter
    def candles(self, candles):
        """
        :param list[clients.tinkoff.models.Candle] candles:
        """
        if candles is None:
            raise ValueError('Invalid value for `candles`, must not be `None`')

        self._candles = candles
