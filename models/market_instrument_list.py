from __future__ import annotations

from . import _base


class MarketInstrumentList(_base.Model):
    swagger_types: dict[str, str] = {
        'total': 'float',
        'instruments': 'list[MarketInstrument]',
    }

    attribute_map: dict[str, str] = {
        'total': 'total',
        'instruments': 'instruments',
    }

    def __init__(self, total=None, instruments=None):
        self._total = None
        self._instruments = None
        self.discriminator = None
        self.total = total
        self.instruments = instruments

    @property
    def total(self):
        """
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        :param float total:
        """
        if total is None:
            raise ValueError('Invalid value for `total`, must not be `None`')

        self._total = total

    @property
    def instruments(self):
        """
        :rtype: list[clients.tinkoff.models.MarketInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """
        :param list[clients.tinkoff.models.MarketInstrument] instruments:
        """
        if instruments is None:
            raise ValueError(
                'Invalid value for `instruments`, must not be `None`'
            )

        self._instruments = instruments
