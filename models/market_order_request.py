from __future__ import annotations

from . import _base


class MarketOrderRequest(_base.Model):
    swagger_types: dict[str, str] = {
        'lots': 'int',
        'operation': 'OperationType',
    }

    attribute_map: dict[str, str] = {'lots': 'lots', 'operation': 'operation'}

    def __init__(self, lots=None, operation=None):
        self._lots = None
        self._operation = None
        self.discriminator = None
        self.lots = lots
        self.operation = operation

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
