from __future__ import annotations

import pprint


class PortfolioPosition(object):
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
        """PortfolioPosition - a model defined in Swagger"""
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
        """Gets the figi of this PortfolioPosition.

        :returns: The figi of this PortfolioPosition.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this PortfolioPosition.

        :param figi: The figi of this PortfolioPosition.
        :type: str
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def ticker(self):
        """Gets the ticker of this PortfolioPosition.

        :returns: The ticker of this PortfolioPosition.
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this PortfolioPosition.

        :param ticker: The ticker of this PortfolioPosition.
        :type: str
        """

        self._ticker = ticker

    @property
    def isin(self):
        """Gets the isin of this PortfolioPosition.

        :returns: The isin of this PortfolioPosition.
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this PortfolioPosition.

        :param isin: The isin of this PortfolioPosition.
        :type: str
        """

        self._isin = isin

    @property
    def instrument_type(self):
        """Gets the instrument_type of this PortfolioPosition.

        :returns: The instrument_type of this PortfolioPosition.
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this PortfolioPosition.

        :param clients.tinkoff.models.InstrumentType instrument_type:
            The instrument_type of this PortfolioPosition.
        """
        if instrument_type is None:
            raise ValueError(
                'Invalid value for `instrument_type`, must not be `None`'
            )

        self._instrument_type = instrument_type

    @property
    def balance(self):
        """Gets the balance of this PortfolioPosition.

        :returns: The balance of this PortfolioPosition.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this PortfolioPosition.

        :param balance: The balance of this PortfolioPosition.
        :type: float
        """
        if balance is None:
            raise ValueError('Invalid value for `balance`, must not be `None`')

        self._balance = balance

    @property
    def blocked(self):
        """Gets the blocked of this PortfolioPosition.

        :returns: The blocked of this PortfolioPosition.
        :rtype: float
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this PortfolioPosition.

        :param blocked: The blocked of this PortfolioPosition.
        :type: float
        """

        self._blocked = blocked

    @property
    def expected_yield(self):
        """Gets the expected_yield of this PortfolioPosition.

        :returns: The expected_yield of this PortfolioPosition.
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._expected_yield

    @expected_yield.setter
    def expected_yield(self, expected_yield):
        """Sets the expected_yield of this PortfolioPosition.

        :param expected_yield: The expected_yield of this PortfolioPosition.
        :type: clients.tinkoff.models.MoneyAmount
        """

        self._expected_yield = expected_yield

    @property
    def lots(self):
        """Gets the lots of this PortfolioPosition.

        :returns: The lots of this PortfolioPosition.
        :rtype: int
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """Sets the lots of this PortfolioPosition.

        :param lots: The lots of this PortfolioPosition.
        :type: int
        """
        if lots is None:
            raise ValueError('Invalid value for `lots`, must not be `None`')

        self._lots = lots

    @property
    def average_position_price(self):
        """Gets the average_position_price of this PortfolioPosition.

        :returns: The average_position_price of this PortfolioPosition.
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._average_position_price

    @average_position_price.setter
    def average_position_price(self, average_position_price):
        """Sets the average_position_price of this PortfolioPosition.

        :param average_position_price: The average_position_price of this PortfolioPosition.
        :type: clients.tinkoff.models.MoneyAmount
        """

        self._average_position_price = average_position_price

    @property
    def average_position_price_no_nkd(self):
        """Gets the average_position_price_no_nkd of this PortfolioPosition.

        :returns: The average_position_price_no_nkd of this PortfolioPosition.
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._average_position_price_no_nkd

    @average_position_price_no_nkd.setter
    def average_position_price_no_nkd(self, average_position_price_no_nkd):
        """Sets the average_position_price_no_nkd of this PortfolioPosition.

        :param average_position_price_no_nkd: The average_position_price_no_nkd of this PortfolioPosition.
        :type: clients.tinkoff.models.MoneyAmount
        """

        self._average_position_price_no_nkd = average_position_price_no_nkd

    @property
    def name(self):
        """Gets the name of this PortfolioPosition.

        :returns: The name of this PortfolioPosition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortfolioPosition.

        :param name: The name of this PortfolioPosition.
        :type: str
        """
        if name is None:
            raise ValueError('Invalid value for `name`, must not be `None`')

        self._name = name

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
        if not isinstance(other, PortfolioPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
