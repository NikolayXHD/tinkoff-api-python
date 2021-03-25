from __future__ import annotations

import pprint


class OperationTrade(object):
    swagger_types: dict[str, str] = {
        'trade_id': 'str',
        '_date': 'datetime',
        'price': 'float',
        'quantity': 'int'
    }

    attribute_map: dict[str, str] = {
        'trade_id': 'tradeId',
        '_date': 'date',
        'price': 'price',
        'quantity': 'quantity'
    }

    def __init__(self, trade_id=None, _date=None, price=None, quantity=None):
        """OperationTrade - a model defined in Swagger"""
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
        """Gets the trade_id of this OperationTrade.

        :returns: The trade_id of this OperationTrade.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this OperationTrade.

        :param trade_id: The trade_id of this OperationTrade.
        :type: str
        """
        if trade_id is None:
            raise ValueError("Invalid value for `trade_id`, must not be `None`")

        self._trade_id = trade_id

    @property
    def _date(self):
        """Gets the _date of this OperationTrade.

        ISO8601
        :returns: The _date of this OperationTrade.
        :rtype: datetime.datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this OperationTrade.

        ISO8601
        :param _date: The _date of this OperationTrade.
         :type: datetime.datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def price(self):
        """Gets the price of this OperationTrade.

        :returns: The price of this OperationTrade.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OperationTrade.

        :param price: The price of this OperationTrade.
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OperationTrade.

        :returns: The quantity of this OperationTrade.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OperationTrade.

        :param quantity: The quantity of this OperationTrade.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

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
        if not isinstance(other, OperationTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
