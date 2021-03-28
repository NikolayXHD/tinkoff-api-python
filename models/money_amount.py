from __future__ import annotations

from . import _base


class MoneyAmount(_base.Model):
    swagger_types: dict[str, str] = {'currency': 'Currency', 'value': 'float'}

    attribute_map: dict[str, str] = {'currency': 'currency', 'value': 'value'}

    def __init__(self, currency=None, value=None):
        self._currency = None
        self._value = None
        self.discriminator = None
        self.currency = currency
        self.value = value

    @property
    def currency(self):
        """
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        :param clients.tinkoff.models.Currency currency:
        """
        if currency is None:
            raise ValueError(
                'Invalid value for `currency`, must not be `None`'
            )

        self._currency = currency

    @property
    def value(self):
        """
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        :param float value:
        """
        if value is None:
            raise ValueError('Invalid value for `value`, must not be `None`')

        self._value = value
