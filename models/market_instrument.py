from __future__ import annotations

import pprint


class MarketInstrument(object):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'ticker': 'str',
        'isin': 'str',
        'min_price_increment': 'float',
        'lot': 'int',
        'min_quantity': 'int',
        'currency': 'Currency',
        'name': 'str',
        'type': 'InstrumentType'
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'ticker': 'ticker',
        'isin': 'isin',
        'min_price_increment': 'minPriceIncrement',
        'lot': 'lot',
        'min_quantity': 'minQuantity',
        'currency': 'currency',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, figi=None, ticker=None, isin=None, min_price_increment=None, lot=None, min_quantity=None, currency=None, name=None, type=None):
        """MarketInstrument - a model defined in Swagger"""
        self._figi = None
        self._ticker = None
        self._isin = None
        self._min_price_increment = None
        self._lot = None
        self._min_quantity = None
        self._currency = None
        self._name = None
        self._type = None
        self.discriminator = None
        self.figi = figi
        self.ticker = ticker
        if isin is not None:
            self.isin = isin
        if min_price_increment is not None:
            self.min_price_increment = min_price_increment
        self.lot = lot
        if min_quantity is not None:
            self.min_quantity = min_quantity
        if currency is not None:
            self.currency = currency
        self.name = name
        self.type = type

    @property
    def figi(self):
        """Gets the figi of this MarketInstrument.

        :returns: The figi of this MarketInstrument.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this MarketInstrument.

        :param figi: The figi of this MarketInstrument.
        :type: str
        """
        if figi is None:
            raise ValueError("Invalid value for `figi`, must not be `None`")

        self._figi = figi

    @property
    def ticker(self):
        """Gets the ticker of this MarketInstrument.

        :returns: The ticker of this MarketInstrument.
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this MarketInstrument.

        :param ticker: The ticker of this MarketInstrument.
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")

        self._ticker = ticker

    @property
    def isin(self):
        """Gets the isin of this MarketInstrument.

        :returns: The isin of this MarketInstrument.
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this MarketInstrument.

        :param isin: The isin of this MarketInstrument.
        :type: str
        """

        self._isin = isin

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this MarketInstrument.

        Шаг цены
        :returns: The min_price_increment of this MarketInstrument.
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this MarketInstrument.

        Шаг цены
        :param min_price_increment: The min_price_increment of this MarketInstrument.
        :type: float
        """

        self._min_price_increment = min_price_increment

    @property
    def lot(self):
        """Gets the lot of this MarketInstrument.

        :returns: The lot of this MarketInstrument.
        :rtype: int
        """
        return self._lot

    @lot.setter
    def lot(self, lot):
        """Sets the lot of this MarketInstrument.

        :param lot: The lot of this MarketInstrument.
        :type: int
        """
        if lot is None:
            raise ValueError("Invalid value for `lot`, must not be `None`")

        self._lot = lot

    @property
    def min_quantity(self):
        """Gets the min_quantity of this MarketInstrument.

        Минимальное число инструментов для покупки должно быть не меньше, чем размер лота х количество лотов
        :returns: The min_quantity of this MarketInstrument.
        :rtype: int
        """
        return self._min_quantity

    @min_quantity.setter
    def min_quantity(self, min_quantity):
        """Sets the min_quantity of this MarketInstrument.

        Минимальное число инструментов для покупки должно быть не меньше, чем размер лота х количество лотов
        :param min_quantity: The min_quantity of this MarketInstrument.
        :type: int
        """

        self._min_quantity = min_quantity

    @property
    def currency(self):
        """Gets the currency of this MarketInstrument.

        :returns: The currency of this MarketInstrument,
                  value of clients.tinkoff.models.Currency
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MarketInstrument.

        :param currency: The currency of this MarketInstrument.
        :type currency: clients.tinkoff.models.Currency
        """

        self._currency = currency

    @property
    def name(self):
        """Gets the name of this MarketInstrument.

        :returns: The name of this MarketInstrument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MarketInstrument.

        :param name: The name of this MarketInstrument.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """Gets the type of this MarketInstrument.

        :returns: The type of this MarketInstrument.
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MarketInstrument.

        :param type: The type of this MarketInstrument.
        :type type: clients.tinkoff.models.InstrumentType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, MarketInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
