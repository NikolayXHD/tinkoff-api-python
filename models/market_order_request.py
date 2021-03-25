from __future__ import annotations

import pprint


class MarketOrderRequest(object):
    swagger_types: dict[str, str] = {
        'lots': 'int',
        'operation': 'OperationType'
    }

    attribute_map: dict[str, str] = {
        'lots': 'lots',
        'operation': 'operation'
    }

    def __init__(self, lots=None, operation=None):
        """MarketOrderRequest - a model defined in Swagger"""
        self._lots = None
        self._operation = None
        self.discriminator = None
        self.lots = lots
        self.operation = operation

    @property
    def lots(self):
        """Gets the lots of this MarketOrderRequest.

        :returns: The lots of this MarketOrderRequest.
        :rtype: int
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """Sets the lots of this MarketOrderRequest.

        :param lots: The lots of this MarketOrderRequest.
        :type: int
        """
        if lots is None:
            raise ValueError("Invalid value for `lots`, must not be `None`")

        self._lots = lots

    @property
    def operation(self):
        """Gets the operation of this MarketOrderRequest.

        :returns: The operation of this MarketOrderRequest.
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this MarketOrderRequest.

        :param operation: The operation of this MarketOrderRequest.
        :type operation: clients.tinkoff.models.OperationType
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")

        self._operation = operation

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
        if not isinstance(other, MarketOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
