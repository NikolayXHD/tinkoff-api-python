from __future__ import annotations

import pprint


class OrderResponse(object):
    swagger_types: dict[str, str] = {
        'price': 'float',
        'quantity': 'int'
    }

    attribute_map: dict[str, str] = {
        'price': 'price',
        'quantity': 'quantity'
    }

    def __init__(self, price=None, quantity=None):
        """OrderResponse - a model defined in Swagger"""
        self._price = None
        self._quantity = None
        self.discriminator = None
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """Gets the price of this OrderResponse.

        :returns: The price of this OrderResponse.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderResponse.

        :param price: The price of this OrderResponse.
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OrderResponse.

        :returns: The quantity of this OrderResponse.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderResponse.

        :param quantity: The quantity of this OrderResponse.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

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
        if not isinstance(other, OrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
