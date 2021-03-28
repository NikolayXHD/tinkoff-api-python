from __future__ import annotations

from . import _base


class Orderbook(_base.Model):
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
        'limit_down': 'float',
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
        'limit_down': 'limitDown',
    }

    def __init__(
        self,
        figi=None,
        depth=None,
        bids=None,
        asks=None,
        trade_status=None,
        min_price_increment=None,
        face_value=None,
        last_price=None,
        close_price=None,
        limit_up=None,
        limit_down=None,
    ):
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
    def depth(self):
        """
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        :param int depth:
        """
        if depth is None:
            raise ValueError('Invalid value for `depth`, must not be `None`')

        self._depth = depth

    @property
    def bids(self):
        """
        :rtype: list[clients.tinkoff.models.OrderResponse]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """
        :param list[clients.tinkoff.models.OrderResponse] bids:
        """
        if bids is None:
            raise ValueError('Invalid value for `bids`, must not be `None`')

        self._bids = bids

    @property
    def asks(self):
        """
        :rtype: list[clients.tinkoff.models.OrderResponse]
        """
        return self._asks

    @asks.setter
    def asks(self, asks):
        """
        :param list[clients.tinkoff.models.OrderResponse] asks:
        """
        if asks is None:
            raise ValueError('Invalid value for `asks`, must not be `None`')

        self._asks = asks

    @property
    def trade_status(self):
        """
        :rtype: clients.tinkoff.models.TradeStatus
        """
        return self._trade_status

    @trade_status.setter
    def trade_status(self, trade_status):
        """
        :param clients.tinkoff.models.TradeStatus trade_status:
        """
        if trade_status is None:
            raise ValueError(
                'Invalid value for `trade_status`, must not be `None`'
            )

        self._trade_status = trade_status

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
        if min_price_increment is None:
            raise ValueError(
                'Invalid value for `min_price_increment`, must not be `None`'
            )

        self._min_price_increment = min_price_increment

    @property
    def face_value(self):
        """
        Номинал для облигаций
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """
        Номинал для облигаций
        :param float face_value:
        """
        self._face_value = face_value

    @property
    def last_price(self):
        """
        :rtype: float
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """
        :param float last_price:
        """
        self._last_price = last_price

    @property
    def close_price(self):
        """
        :rtype: float
        """
        return self._close_price

    @close_price.setter
    def close_price(self, close_price):
        """
        :param float close_price:
        """
        self._close_price = close_price

    @property
    def limit_up(self):
        """
        Верхняя граница цены
        :rtype: float
        """
        return self._limit_up

    @limit_up.setter
    def limit_up(self, limit_up):
        """
        Верхняя граница цены
        :param float limit_up:
        """
        self._limit_up = limit_up

    @property
    def limit_down(self):
        """
        Нижняя граница цены
        :rtype: float
        """
        return self._limit_down

    @limit_down.setter
    def limit_down(self, limit_down):
        """
        Нижняя граница цены
        :param float limit_down:
        """
        self._limit_down = limit_down
