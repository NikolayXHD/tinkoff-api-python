from __future__ import annotations

import pprint


class LimitOrderRequest(object):
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
        """LimitOrderRequest - a model defined in Swagger"""
        self._lots = None
        self._operation = None
        self._price = None
        self.discriminator = None
        self.lots = lots
        self.operation = operation
        self.price = price

    @property
    def lots(self):
        """Gets the lots of this LimitOrderRequest.

        :returns: The lots of this LimitOrderRequest.
        :rtype: int
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """Sets the lots of this LimitOrderRequest.

        :param lots: The lots of this LimitOrderRequest.
        :type: int
        """
        if lots is None:
            raise ValueError('Invalid value for `lots`, must not be `None`')

        self._lots = lots

    @property
    def operation(self):
        """Gets the operation of this LimitOrderRequest.

        :returns: The operation of this LimitOrderRequest.
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this LimitOrderRequest.

        :param clients.tinkoff.models.OperationType operation:
            The operation of this LimitOrderRequest.
        """
        if operation is None:
            raise ValueError(
                'Invalid value for `operation`, must not be `None`'
            )

        self._operation = operation

    @property
    def price(self):
        """Gets the price of this LimitOrderRequest.

        :returns: The price of this LimitOrderRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LimitOrderRequest.

        :param price: The price of this LimitOrderRequest.
        :type: float
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
        if not isinstance(other, LimitOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
