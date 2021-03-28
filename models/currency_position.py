from __future__ import annotations

from . import _base


class CurrencyPosition(_base.Model):
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
    def balance(self):
        """
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        :param float balance:
        """
        if balance is None:
            raise ValueError('Invalid value for `balance`, must not be `None`')

        self._balance = balance

    @property
    def blocked(self):
        """
        :rtype: float
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """
        :param float blocked:
        """
        self._blocked = blocked
