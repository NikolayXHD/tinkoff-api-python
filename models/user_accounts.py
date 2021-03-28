from __future__ import annotations

from . import _base


class UserAccounts(_base.Model):
    swagger_types: dict[str, str] = {'accounts': 'list[UserAccount]'}

    attribute_map: dict[str, str] = {'accounts': 'accounts'}

    def __init__(self, accounts=None):
        self._accounts = None
        self.discriminator = None
        self.accounts = accounts

    @property
    def accounts(self):
        """
        :rtype: list[clients.tinkoff.models.UserAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """
        :param list[clients.tinkoff.models.UserAccount] accounts:
        """
        if accounts is None:
            raise ValueError(
                'Invalid value for `accounts`, must not be `None`'
            )

        self._accounts = accounts
