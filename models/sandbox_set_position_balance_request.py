from __future__ import annotations

from . import _base


class SandboxSetPositionBalanceRequest(_base.Model):
    swagger_types: dict[str, str] = {'figi': 'str', 'balance': 'float'}

    attribute_map: dict[str, str] = {'figi': 'figi', 'balance': 'balance'}

    def __init__(self, figi=None, balance=None):
        self._figi = None
        self._balance = None
        self.discriminator = None
        if figi is not None:
            self.figi = figi
        self.balance = balance

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
        self._figi = figi

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
