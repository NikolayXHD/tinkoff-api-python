from __future__ import annotations

from . import _base


class Currencies(_base.Model):
    swagger_types: dict[str, str] = {'currencies': 'list[CurrencyPosition]'}

    attribute_map: dict[str, str] = {'currencies': 'currencies'}

    def __init__(self, currencies=None):
        self._currencies = None
        self.discriminator = None
        self.currencies = currencies

    @property
    def currencies(self):
        """
        :rtype: list[clients.tinkoff.models.CurrencyPosition]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """
        :param list[clients.tinkoff.models.CurrencyPosition] currencies:
        """
        if currencies is None:
            raise ValueError(
                'Invalid value for `currencies`, must not be `None`'
            )

        self._currencies = currencies
