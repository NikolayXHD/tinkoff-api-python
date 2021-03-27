from __future__ import annotations

import pprint


class SearchMarketInstrument(object):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'ticker': 'str',
        'isin': 'str',
        'min_price_increment': 'float',
        'lot': 'int',
        'currency': 'Currency',
        'name': 'str',
        'type': 'InstrumentType',
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'ticker': 'ticker',
        'isin': 'isin',
        'min_price_increment': 'minPriceIncrement',
        'lot': 'lot',
        'currency': 'currency',
        'name': 'name',
        'type': 'type',
    }

    def __init__(
        self,
        figi=None,
        ticker=None,
        isin=None,
        min_price_increment=None,
        lot=None,
        currency=None,
        name=None,
        type=None,
    ):
        """SearchMarketInstrument - a model defined in Swagger"""
        self._figi = None
        self._ticker = None
        self._isin = None
        self._min_price_increment = None
        self._lot = None
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
        if currency is not None:
            self.currency = currency
        self.name = name
        self.type = type

    @property
    def figi(self):
        """Gets the figi of this SearchMarketInstrument.

        :returns: The figi of this SearchMarketInstrument.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this SearchMarketInstrument.

        :param figi: The figi of this SearchMarketInstrument.
        :type: str
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def ticker(self):
        """Gets the ticker of this SearchMarketInstrument.

        :returns: The ticker of this SearchMarketInstrument.
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SearchMarketInstrument.

        :param ticker: The ticker of this SearchMarketInstrument.
        :type: str
        """
        if ticker is None:
            raise ValueError('Invalid value for `ticker`, must not be `None`')

        self._ticker = ticker

    @property
    def isin(self):
        """Gets the isin of this SearchMarketInstrument.

        :returns: The isin of this SearchMarketInstrument.
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this SearchMarketInstrument.

        :param isin: The isin of this SearchMarketInstrument.
        :type: str
        """

        self._isin = isin

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this SearchMarketInstrument.

        Шаг цены
        :returns: The min_price_increment of this SearchMarketInstrument.
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this SearchMarketInstrument.

        Шаг цены
        :param min_price_increment: The min_price_increment of this SearchMarketInstrument.
        :type: float
        """

        self._min_price_increment = min_price_increment

    @property
    def lot(self):
        """Gets the lot of this SearchMarketInstrument.

        :returns: The lot of this SearchMarketInstrument.
        :rtype: int
        """
        return self._lot

    @lot.setter
    def lot(self, lot):
        """Sets the lot of this SearchMarketInstrument.

        :param lot: The lot of this SearchMarketInstrument.
        :type: int
        """
        if lot is None:
            raise ValueError('Invalid value for `lot`, must not be `None`')

        self._lot = lot

    @property
    def currency(self):
        """Gets the currency of this SearchMarketInstrument.

        :returns: The currency of this SearchMarketInstrument.
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SearchMarketInstrument.

        :param clients.tinkoff.models.Currency currency:
            The currency of this SearchMarketInstrument.
        """

        self._currency = currency

    @property
    def name(self):
        """Gets the name of this SearchMarketInstrument.

        :returns: The name of this SearchMarketInstrument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchMarketInstrument.

        :param name: The name of this SearchMarketInstrument.
        :type: str
        """
        if name is None:
            raise ValueError('Invalid value for `name`, must not be `None`')

        self._name = name

    @property
    def type(self):
        """Gets the type of this SearchMarketInstrument.

        :returns: The type of this SearchMarketInstrument.
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchMarketInstrument.

        :param clients.tinkoff.models.InstrumentType type:
            The type of this SearchMarketInstrument.
        """
        if type is None:
            raise ValueError('Invalid value for `type`, must not be `None`')

        self._type = type

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
        if not isinstance(other, SearchMarketInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
