from __future__ import annotations

from . import _base


class OrderResponse(_base.Model):
    swagger_types: dict[str, str] = {'price': 'float', 'quantity': 'int'}

    attribute_map: dict[str, str] = {'price': 'price', 'quantity': 'quantity'}

    def __init__(self, price=None, quantity=None):
        self._price = None
        self._quantity = None
        self.discriminator = None
        self.price = price
        self.quantity = quantity

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

    @property
    def quantity(self):
        """
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        :param int quantity:
        """
        if quantity is None:
            raise ValueError(
                'Invalid value for `quantity`, must not be `None`'
            )

        self._quantity = quantity
