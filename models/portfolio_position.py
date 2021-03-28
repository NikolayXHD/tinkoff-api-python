from __future__ import annotations

from . import _base


class PortfolioPosition(_base.Model):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'ticker': 'str',
        'isin': 'str',
        'instrument_type': 'InstrumentType',
        'balance': 'float',
        'blocked': 'float',
        'expected_yield': 'MoneyAmount',
        'lots': 'int',
        'average_position_price': 'MoneyAmount',
        'average_position_price_no_nkd': 'MoneyAmount',
        'name': 'str',
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'ticker': 'ticker',
        'isin': 'isin',
        'instrument_type': 'instrumentType',
        'balance': 'balance',
        'blocked': 'blocked',
        'expected_yield': 'expectedYield',
        'lots': 'lots',
        'average_position_price': 'averagePositionPrice',
        'average_position_price_no_nkd': 'averagePositionPriceNoNkd',
        'name': 'name',
    }

    def __init__(
        self,
        figi=None,
        ticker=None,
        isin=None,
        instrument_type=None,
        balance=None,
        blocked=None,
        expected_yield=None,
        lots=None,
        average_position_price=None,
        average_position_price_no_nkd=None,
        name=None,
    ):
        self._figi = None
        self._ticker = None
        self._isin = None
        self._instrument_type = None
        self._balance = None
        self._blocked = None
        self._expected_yield = None
        self._lots = None
        self._average_position_price = None
        self._average_position_price_no_nkd = None
        self._name = None
        self.discriminator = None
        self.figi = figi
        if ticker is not None:
            self.ticker = ticker
        if isin is not None:
            self.isin = isin
        self.instrument_type = instrument_type
        self.balance = balance
        if blocked is not None:
            self.blocked = blocked
        if expected_yield is not None:
            self.expected_yield = expected_yield
        self.lots = lots
        if average_position_price is not None:
            self.average_position_price = average_position_price
        if average_position_price_no_nkd is not None:
            self.average_position_price_no_nkd = average_position_price_no_nkd
        self.name = name

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
    def ticker(self):
        """
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """
        :param str ticker:
        """
        self._ticker = ticker

    @property
    def isin(self):
        """
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """
        :param str isin:
        """
        self._isin = isin

    @property
    def instrument_type(self):
        """
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """
        :param clients.tinkoff.models.InstrumentType instrument_type:
        """
        if instrument_type is None:
            raise ValueError(
                'Invalid value for `instrument_type`, must not be `None`'
            )

        self._instrument_type = instrument_type

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

    @property
    def expected_yield(self):
        """
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._expected_yield

    @expected_yield.setter
    def expected_yield(self, expected_yield):
        """
        :param clients.tinkoff.models.MoneyAmount expected_yield:
        """
        self._expected_yield = expected_yield

    @property
    def lots(self):
        """
        :rtype: int
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """
        :param int lots:
        """
        if lots is None:
            raise ValueError('Invalid value for `lots`, must not be `None`')

        self._lots = lots

    @property
    def average_position_price(self):
        """
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._average_position_price

    @average_position_price.setter
    def average_position_price(self, average_position_price):
        """
        :param clients.tinkoff.models.MoneyAmount average_position_price:
        """
        self._average_position_price = average_position_price

    @property
    def average_position_price_no_nkd(self):
        """
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._average_position_price_no_nkd

    @average_position_price_no_nkd.setter
    def average_position_price_no_nkd(self, avg_position_price_no_nkd):
        """
        :param clients.tinkoff.models.MoneyAmount avg_position_price_no_nkd:
        """
        self._average_position_price_no_nkd = avg_position_price_no_nkd

    @property
    def name(self):
        """
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        :param str name:
        """
        if name is None:
            raise ValueError('Invalid value for `name`, must not be `None`')

        self._name = name
