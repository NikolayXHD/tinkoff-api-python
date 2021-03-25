from __future__ import annotations

import pprint


class UserAccounts(object):
    swagger_types: dict[str, str] = {
        'accounts': 'list[UserAccount]'
    }

    attribute_map: dict[str, str] = {
        'accounts': 'accounts'
    }

    def __init__(self, accounts=None):
        """UserAccounts - a model defined in Swagger"""
        self._accounts = None
        self.discriminator = None
        self.accounts = accounts

    @property
    def accounts(self):
        """Gets the accounts of this UserAccounts.

        :returns: The accounts of this UserAccounts.
        :rtype: list[clients.tinkoff.models.UserAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this UserAccounts.

        :param accounts: The accounts of this UserAccounts.
        :type: list[clients.tinkoff.models.UserAccount]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")

        self._accounts = accounts

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
        if not isinstance(other, UserAccounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
