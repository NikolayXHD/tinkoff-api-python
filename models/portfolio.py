from __future__ import annotations

import pprint


class Portfolio(object):
    swagger_types: dict[str, str] = {'positions': 'list[PortfolioPosition]'}

    attribute_map: dict[str, str] = {'positions': 'positions'}

    def __init__(self, positions=None):
        """Portfolio - a model defined in Swagger"""
        self._positions = None
        self.discriminator = None
        self.positions = positions

    @property
    def positions(self):
        """Gets the positions of this Portfolio.

        :returns: The positions of this Portfolio.
        :rtype: list[clients.tinkoff.models.PortfolioPosition]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this Portfolio.

        :param list[clients.tinkoff.models.PortfolioPosition] positions: The positions of this Portfolio.
        """
        if positions is None:
            raise ValueError(
                'Invalid value for `positions`, must not be `None`'
            )

        self._positions = positions

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
        if not isinstance(other, Portfolio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
