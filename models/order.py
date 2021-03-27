from __future__ import annotations

import pprint


class Order(object):
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
        """Order - a model defined in Swagger"""
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
        """Gets the order_id of this Order.

        :returns: The order_id of this Order.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        :param str order_id: The order_id of this Order.
        """
        if order_id is None:
            raise ValueError(
                'Invalid value for `order_id`, must not be `None`'
            )

        self._order_id = order_id

    @property
    def figi(self):
        """Gets the figi of this Order.

        :returns: The figi of this Order.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Order.

        :param str figi: The figi of this Order.
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def operation(self):
        """Gets the operation of this Order.

        :returns: The operation of this Order.
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Order.

        :param clients.tinkoff.models.OperationType operation:
            The operation of this Order.
        """
        if operation is None:
            raise ValueError(
                'Invalid value for `operation`, must not be `None`'
            )

        self._operation = operation

    @property
    def status(self):
        """Gets the status of this Order.

        :returns: The status of this Order.
        :rtype: clients.tinkoff.models.OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        :param clients.tinkoff.models.OrderStatus status: The status of this Order.
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def requested_lots(self):
        """Gets the requested_lots of this Order.

        :returns: The requested_lots of this Order.
        :rtype: int
        """
        return self._requested_lots

    @requested_lots.setter
    def requested_lots(self, requested_lots):
        """Sets the requested_lots of this Order.

        :param int requested_lots: The requested_lots of this Order.
        """
        if requested_lots is None:
            raise ValueError(
                'Invalid value for `requested_lots`, must not be `None`'
            )

        self._requested_lots = requested_lots

    @property
    def executed_lots(self):
        """Gets the executed_lots of this Order.

        :returns: The executed_lots of this Order.
        :rtype: int
        """
        return self._executed_lots

    @executed_lots.setter
    def executed_lots(self, executed_lots):
        """Sets the executed_lots of this Order.

        :param int executed_lots: The executed_lots of this Order.
        """
        if executed_lots is None:
            raise ValueError(
                'Invalid value for `executed_lots`, must not be `None`'
            )

        self._executed_lots = executed_lots

    @property
    def type(self):
        """Gets the type of this Order.

        :returns: The type of this Order.
        :rtype: clients.tinkoff.models.OrderType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.

        :param clients.tinkoff.models.OrderType type: The type of this Order.
        """
        if type is None:
            raise ValueError('Invalid value for `type`, must not be `None`')

        self._type = type

    @property
    def price(self):
        """Gets the price of this Order.

        :returns: The price of this Order.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.

        :param float price: The price of this Order.
        """
        if price is None:
            raise ValueError('Invalid value for `price`, must not be `None`')

        self._price = price

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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
