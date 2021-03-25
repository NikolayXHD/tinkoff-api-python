from __future__ import annotations

import pprint


class Orderbook(object):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'depth': 'int',
        'bids': 'list[OrderResponse]',
        'asks': 'list[OrderResponse]',
        'trade_status': 'TradeStatus',
        'min_price_increment': 'float',
        'face_value': 'float',
        'last_price': 'float',
        'close_price': 'float',
        'limit_up': 'float',
        'limit_down': 'float'
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'depth': 'depth',
        'bids': 'bids',
        'asks': 'asks',
        'trade_status': 'tradeStatus',
        'min_price_increment': 'minPriceIncrement',
        'face_value': 'faceValue',
        'last_price': 'lastPrice',
        'close_price': 'closePrice',
        'limit_up': 'limitUp',
        'limit_down': 'limitDown'
    }

    def __init__(self, figi=None, depth=None, bids=None, asks=None, trade_status=None, min_price_increment=None, face_value=None, last_price=None, close_price=None, limit_up=None, limit_down=None):
        """Orderbook - a model defined in Swagger"""
        self._figi = None
        self._depth = None
        self._bids = None
        self._asks = None
        self._trade_status = None
        self._min_price_increment = None
        self._face_value = None
        self._last_price = None
        self._close_price = None
        self._limit_up = None
        self._limit_down = None
        self.discriminator = None
        self.figi = figi
        self.depth = depth
        self.bids = bids
        self.asks = asks
        self.trade_status = trade_status
        self.min_price_increment = min_price_increment
        if face_value is not None:
            self.face_value = face_value
        if last_price is not None:
            self.last_price = last_price
        if close_price is not None:
            self.close_price = close_price
        if limit_up is not None:
            self.limit_up = limit_up
        if limit_down is not None:
            self.limit_down = limit_down

    @property
    def figi(self):
        """Gets the figi of this Orderbook.

        :returns: The figi of this Orderbook.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Orderbook.

        :param figi: The figi of this Orderbook.
        :type: str
        """
        if figi is None:
            raise ValueError("Invalid value for `figi`, must not be `None`")

        self._figi = figi

    @property
    def depth(self):
        """Gets the depth of this Orderbook.

        :returns: The depth of this Orderbook.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Orderbook.

        :param depth: The depth of this Orderbook.
        :type: int
        """
        if depth is None:
            raise ValueError("Invalid value for `depth`, must not be `None`")

        self._depth = depth

    @property
    def bids(self):
        """Gets the bids of this Orderbook.

        :returns: The bids of this Orderbook.
        :rtype: list[clients.tinkoff.models.OrderResponse]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this Orderbook.

        :param bids: The bids of this Orderbook.
        :type: list[clients.tinkoff.models.OrderResponse]
        """
        if bids is None:
            raise ValueError("Invalid value for `bids`, must not be `None`")

        self._bids = bids

    @property
    def asks(self):
        """Gets the asks of this Orderbook.

        :returns: The asks of this Orderbook.
        :rtype: list[clients.tinkoff.models.OrderResponse]
        """
        return self._asks

    @asks.setter
    def asks(self, asks):
        """Sets the asks of this Orderbook.

        :param asks: The asks of this Orderbook.
        :type: list[clients.tinkoff.models.OrderResponse]
        """
        if asks is None:
            raise ValueError("Invalid value for `asks`, must not be `None`")

        self._asks = asks

    @property
    def trade_status(self):
        """Gets the trade_status of this Orderbook.

        :returns: The trade_status of this Orderbook.
        :rtype: clients.tinkoff.models.TradeStatus
        """
        return self._trade_status

    @trade_status.setter
    def trade_status(self, trade_status):
        """Sets the trade_status of this Orderbook.

        :param trade_status: The trade_status of this Orderbook.
        :type: clients.tinkoff.models.TradeStatus
        """
        if trade_status is None:
            raise ValueError("Invalid value for `trade_status`, must not be `None`")

        self._trade_status = trade_status

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this Orderbook.

        Шаг цены
        :returns: The min_price_increment of this Orderbook.
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this Orderbook.

        Шаг цены
        :param min_price_increment: The min_price_increment of this Orderbook.
        :type: float
        """
        if min_price_increment is None:
            raise ValueError("Invalid value for `min_price_increment`, must not be `None`")

        self._min_price_increment = min_price_increment

    @property
    def face_value(self):
        """Gets the face_value of this Orderbook.

        Номинал для облигаций
        :returns: The face_value of this Orderbook.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this Orderbook.

        Номинал для облигаций
        :param face_value: The face_value of this Orderbook.
        :type: float
        """

        self._face_value = face_value

    @property
    def last_price(self):
        """Gets the last_price of this Orderbook.

        :returns: The last_price of this Orderbook.
        :rtype: float
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this Orderbook.

        :param last_price: The last_price of this Orderbook.
        :type: float
        """

        self._last_price = last_price

    @property
    def close_price(self):
        """Gets the close_price of this Orderbook.

        :returns: The close_price of this Orderbook.
        :rtype: float
        """
        return self._close_price

    @close_price.setter
    def close_price(self, close_price):
        """Sets the close_price of this Orderbook.

        :param close_price: The close_price of this Orderbook.
        :type: float
        """

        self._close_price = close_price

    @property
    def limit_up(self):
        """Gets the limit_up of this Orderbook.

        Верхняя граница цены
        :returns: The limit_up of this Orderbook.
        :rtype: float
        """
        return self._limit_up

    @limit_up.setter
    def limit_up(self, limit_up):
        """Sets the limit_up of this Orderbook.

        Верхняя граница цены
        :param limit_up: The limit_up of this Orderbook.
        :type: float
        """

        self._limit_up = limit_up

    @property
    def limit_down(self):
        """Gets the limit_down of this Orderbook.

        Нижняя граница цены
        :returns: The limit_down of this Orderbook.
        :rtype: float
        """
        return self._limit_down

    @limit_down.setter
    def limit_down(self, limit_down):
        """Sets the limit_down of this Orderbook.

        Нижняя граница цены
        :param limit_down: The limit_down of this Orderbook.
        :type: float
        """

        self._limit_down = limit_down

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
        if not isinstance(other, Orderbook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
