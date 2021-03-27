from __future__ import annotations

import pprint


class Operations(object):
    swagger_types: dict[str, str] = {'operations': 'list[Operation]'}

    attribute_map: dict[str, str] = {'operations': 'operations'}

    def __init__(self, operations=None):
        """Operations - a model defined in Swagger"""
        self._operations = None
        self.discriminator = None
        self.operations = operations

    @property
    def operations(self):
        """Gets the operations of this Operations.

        :returns: The operations of this Operations.
        :rtype: list[clients.tinkoff.models.Operation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this Operations.

        :param list[clients.tinkoff.models.Operation] operations: The operations of this Operations.
        """
        if operations is None:
            raise ValueError(
                'Invalid value for `operations`, must not be `None`'
            )

        self._operations = operations

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
        if not isinstance(other, Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
