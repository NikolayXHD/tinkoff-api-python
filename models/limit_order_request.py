from __future__ import annotations

from . import _base


class LimitOrderRequest(_base.Model):
    swagger_types: dict[str, str] = {
        'lots': 'int',
        'operation': 'OperationType',
        'price': 'float',
    }

    attribute_map: dict[str, str] = {
        'lots': 'lots',
        'operation': 'operation',
        'price': 'price',
    }

    def __init__(self, lots=None, operation=None, price=None):
        self._lots = None
        self._operation = None
        self._price = None
        self.discriminator = None
        self.lots = lots
        self.operation = operation
        self.price = price

    @property
    def lots(self):
        """
        :rtype: int
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """
        :param int lots:
        """
        if lots is None:
            raise ValueError('Invalid value for `lots`, must not be `None`')

        self._lots = lots

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
