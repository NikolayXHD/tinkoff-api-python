from __future__ import annotations

from . import _base


class SandboxAccount(_base.Model):
    swagger_types: dict[str, str] = {
        'broker_account_type': 'BrokerAccountType',
        'broker_account_id': 'str',
    }

    attribute_map: dict[str, str] = {
        'broker_account_type': 'brokerAccountType',
        'broker_account_id': 'brokerAccountId',
    }

    def __init__(self, broker_account_type=None, broker_account_id=None):
        self._broker_account_type = None
        self._broker_account_id = None
        self.discriminator = None
        self.broker_account_type = broker_account_type
        self.broker_account_id = broker_account_id

    @property
    def broker_account_type(self):
        """
        :rtype: clients.tinkoff.models.BrokerAccountType
        """
        return self._broker_account_type

    @broker_account_type.setter
    def broker_account_type(self, broker_account_type):
        """
        :param clients.tinkoff.models.BrokerAccountType broker_account_type:
        """
        if broker_account_type is None:
            raise ValueError(
                'Invalid value for `broker_account_type`, must not be `None`'
            )

        self._broker_account_type = broker_account_type

    @property
    def broker_account_id(self):
        """
        :rtype: str
        """
        return self._broker_account_id

    @broker_account_id.setter
    def broker_account_id(self, broker_account_id):
        """
        :param str broker_account_id:
        """
        if broker_account_id is None:
            raise ValueError(
                'Invalid value for `broker_account_id`, must not be `None`'
            )

        self._broker_account_id = broker_account_id
