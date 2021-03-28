from __future__ import annotations

from . import _base


class Portfolio(_base.Model):
    swagger_types: dict[str, str] = {'positions': 'list[PortfolioPosition]'}

    attribute_map: dict[str, str] = {'positions': 'positions'}

    def __init__(self, positions=None):
        self._positions = None
        self.discriminator = None
        self.positions = positions

    @property
    def positions(self):
        """
        :rtype: list[clients.tinkoff.models.PortfolioPosition]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """
        :param list[clients.tinkoff.models.PortfolioPosition] positions:
        """
        if positions is None:
            raise ValueError(
                'Invalid value for `positions`, must not be `None`'
            )

        self._positions = positions
