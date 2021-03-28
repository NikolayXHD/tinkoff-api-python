from __future__ import annotations

from . import _base


class SandboxSetCurrencyBalanceRequest(_base.Model):
    swagger_types: dict[str, str] = {
        'currency': 'SandboxCurrency',
        'balance': 'float',
    }

    attribute_map: dict[str, str] = {
        'currency': 'currency',
        'balance': 'balance',
    }

    def __init__(self, currency=None, balance=None):
        self._currency = None
        self._balance = None
        self.discriminator = None
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        """
        :rtype: clients.tinkoff.models.SandboxCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        :param clients.tinkoff.models.SandboxCurrency currency:
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
