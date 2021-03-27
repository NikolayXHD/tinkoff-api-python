from __future__ import annotations

import pprint


class SandboxSetPositionBalanceRequest(object):
    swagger_types: dict[str, str] = {'figi': 'str', 'balance': 'float'}

    attribute_map: dict[str, str] = {'figi': 'figi', 'balance': 'balance'}

    def __init__(self, figi=None, balance=None):
        """SandboxSetPositionBalanceRequest - a model defined in Swagger"""
        self._figi = None
        self._balance = None
        self.discriminator = None
        if figi is not None:
            self.figi = figi
        self.balance = balance

    @property
    def figi(self):
        """Gets the figi of this SandboxSetPositionBalanceRequest.

        :returns: The figi of this SandboxSetPositionBalanceRequest.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this SandboxSetPositionBalanceRequest.

        :param str figi: The figi of this SandboxSetPositionBalanceRequest.
        """

        self._figi = figi

    @property
    def balance(self):
        """Gets the balance of this SandboxSetPositionBalanceRequest.

        :returns: The balance of this SandboxSetPositionBalanceRequest.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SandboxSetPositionBalanceRequest.

        :param float balance: The balance of this SandboxSetPositionBalanceRequest.
        """
        if balance is None:
            raise ValueError('Invalid value for `balance`, must not be `None`')

        self._balance = balance

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
        if not isinstance(other, SandboxSetPositionBalanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
