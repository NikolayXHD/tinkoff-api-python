from __future__ import annotations

from . import _base


class Order(_base.Model):
    swagger_types: dict[str, str] = {
        'order_id': 'str',
        'figi': 'str',
        'operation': 'OperationType',
        'status': 'OrderStatus',
        'requested_lots': 'int',
        'executed_lots': 'int',
        'type': 'OrderType',
        'price': 'float',
    }

    attribute_map: dict[str, str] = {
        'order_id': 'orderId',
        'figi': 'figi',
        'operation': 'operation',
        'status': 'status',
        'requested_lots': 'requestedLots',
        'executed_lots': 'executedLots',
        'type': 'type',
        'price': 'price',
    }

    def __init__(
        self,
        order_id=None,
        figi=None,
        operation=None,
        status=None,
        requested_lots=None,
        executed_lots=None,
        type=None,
        price=None,
    ):
        self._order_id = None
        self._figi = None
        self._operation = None
        self._status = None
        self._requested_lots = None
        self._executed_lots = None
        self._type = None
        self._price = None
        self.discriminator = None
        self.order_id = order_id
        self.figi = figi
        self.operation = operation
        self.status = status
        self.requested_lots = requested_lots
        self.executed_lots = executed_lots
        self.type = type
        self.price = price

    @property
    def order_id(self):
        """
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        :param str order_id:
        """
        if order_id is None:
            raise ValueError(
                'Invalid value for `order_id`, must not be `None`'
            )

        self._order_id = order_id

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
    def operation(self):
        """
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        :param clients.tinkoff.models.OperationType operation:
        """
        if operation is None:
            raise ValueError(
                'Invalid value for `operation`, must not be `None`'
            )

        self._operation = operation

    @property
    def status(self):
        """
        :rtype: clients.tinkoff.models.OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param clients.tinkoff.models.OrderStatus status:
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def requested_lots(self):
        """
        :rtype: int
        """
        return self._requested_lots

    @requested_lots.setter
    def requested_lots(self, requested_lots):
        """
        :param int requested_lots:
        """
        if requested_lots is None:
            raise ValueError(
                'Invalid value for `requested_lots`, must not be `None`'
            )

        self._requested_lots = requested_lots

    @property
    def executed_lots(self):
        """
        :rtype: int
        """
        return self._executed_lots

    @executed_lots.setter
    def executed_lots(self, executed_lots):
        """
        :param int executed_lots:
        """
        if executed_lots is None:
            raise ValueError(
                'Invalid value for `executed_lots`, must not be `None`'
            )

        self._executed_lots = executed_lots

    @property
    def type(self):
        """
        :rtype: clients.tinkoff.models.OrderType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        :param clients.tinkoff.models.OrderType type:
        """
        if type is None:
            raise ValueError('Invalid value for `type`, must not be `None`')

        self._type = type

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
