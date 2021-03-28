from __future__ import annotations

from . import _base


class SandboxRegisterRequest(_base.Model):
    swagger_types: dict[str, str] = {
        'broker_account_type': 'BrokerAccountType'
    }

    attribute_map: dict[str, str] = {
        'broker_account_type': 'brokerAccountType'
    }

    def __init__(self, broker_account_type=None):
        self._broker_account_type = None
        self.discriminator = None
        if broker_account_type is not None:
            self.broker_account_type = broker_account_type

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
        self._broker_account_type = broker_account_type
