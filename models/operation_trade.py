from __future__ import annotations

from . import _base


class OperationTrade(_base.Model):
    swagger_types: dict[str, str] = {
        'trade_id': 'str',
        '_date': 'datetime',
        'price': 'float',
        'quantity': 'int',
    }

    attribute_map: dict[str, str] = {
        'trade_id': 'tradeId',
        '_date': 'date',
        'price': 'price',
        'quantity': 'quantity',
    }

    def __init__(self, trade_id=None, _date=None, price=None, quantity=None):
        self._trade_id = None
        self.__date = None
        self._price = None
        self._quantity = None
        self.discriminator = None
        self.trade_id = trade_id
        self._date = _date
        self.price = price
        self.quantity = quantity

    @property
    def trade_id(self):
        """
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """
        :param str trade_id:
        """
        if trade_id is None:
            raise ValueError(
                'Invalid value for `trade_id`, must not be `None`'
            )

        self._trade_id = trade_id

    @property
    def _date(self):
        """
        ISO8601
        :rtype: datetime.datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """
        ISO8601
        :param datetime.datetime _date:
        """
        if _date is None:
            raise ValueError('Invalid value for `_date`, must not be `None`')

        self.__date = _date

    @property
    def price(self):
        """
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        :param float price:
        """
        if price is None:
            raise ValueError('Invalid value for `price`, must not be `None`')

        self._price = price

    @property
    def quantity(self):
        """
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        :param int quantity:
        """
        if quantity is None:
            raise ValueError(
                'Invalid value for `quantity`, must not be `None`'
            )

        self._quantity = quantity
