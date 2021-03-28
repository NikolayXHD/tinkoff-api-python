from __future__ import annotations

from . import _base


class SearchMarketInstrument(_base.Model):
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
        instr_type=None,
    ):
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
        self.type = instr_type

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
        if ticker is None:
            raise ValueError('Invalid value for `ticker`, must not be `None`')

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
    def min_price_increment(self):
        """
        Шаг цены
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """
        Шаг цены
        :param float min_price_increment:
        """
        self._min_price_increment = min_price_increment

    @property
    def lot(self):
        """
        :rtype: int
        """
        return self._lot

    @lot.setter
    def lot(self, lot):
        """
        :param int lot:
        """
        if lot is None:
            raise ValueError('Invalid value for `lot`, must not be `None`')

        self._lot = lot

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
        self._currency = currency

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

    @property
    def type(self):
        """
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._type

    @type.setter
    def type(self, instr_type):
        """
        :param clients.tinkoff.models.InstrumentType instr_type:
        """
        if instr_type is None:
            raise ValueError('Invalid value for `type`, must not be `None`')

        self._type = instr_type
