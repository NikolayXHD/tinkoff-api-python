from __future__ import annotations

from . import _base


class Operations(_base.Model):
    swagger_types: dict[str, str] = {'operations': 'list[Operation]'}

    attribute_map: dict[str, str] = {'operations': 'operations'}

    def __init__(self, operations=None):
        self._operations = None
        self.discriminator = None
        self.operations = operations

    @property
    def operations(self):
        """
        :rtype: list[clients.tinkoff.models.Operation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        :param list[clients.tinkoff.models.Operation] operations:
        """
        if operations is None:
            raise ValueError(
                'Invalid value for `operations`, must not be `None`'
            )

        self._operations = operations
