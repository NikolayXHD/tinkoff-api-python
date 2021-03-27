from __future__ import annotations

import pprint


class SandboxRegisterRequest(object):
    swagger_types: dict[str, str] = {
        'broker_account_type': 'BrokerAccountType'
    }

    attribute_map: dict[str, str] = {
        'broker_account_type': 'brokerAccountType'
    }

    def __init__(self, broker_account_type=None):
        """SandboxRegisterRequest - a model defined in Swagger"""
        self._broker_account_type = None
        self.discriminator = None
        if broker_account_type is not None:
            self.broker_account_type = broker_account_type

    @property
    def broker_account_type(self):
        """Gets the broker_account_type of this SandboxRegisterRequest.

        :returns: The broker_account_type of this SandboxRegisterRequest.
        :rtype: clients.tinkoff.models.BrokerAccountType
        """
        return self._broker_account_type

    @broker_account_type.setter
    def broker_account_type(self, broker_account_type):
        """Sets the broker_account_type of this SandboxRegisterRequest.

        :param clients.tinkoff.models.BrokerAccountType broker_account_type: The broker_account_type of this SandboxRegisterRequest.
        """

        self._broker_account_type = broker_account_type

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
        if not isinstance(other, SandboxRegisterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
