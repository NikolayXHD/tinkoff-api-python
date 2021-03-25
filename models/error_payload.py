from __future__ import annotations

import pprint


class ErrorPayload(object):
    swagger_types: dict[str, str] = {
        'message': 'str',
        'code': 'str'
    }

    attribute_map: dict[str, str] = {
        'message': 'message',
        'code': 'code'
    }

    def __init__(self, message=None, code=None):
        """ErrorPayload - a model defined in Swagger"""
        self._message = None
        self._code = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    @property
    def message(self):
        """Gets the message of this ErrorPayload.

        :returns: The message of this ErrorPayload.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorPayload.

        :param message: The message of this ErrorPayload.
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this ErrorPayload.

        :returns: The code of this ErrorPayload.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorPayload.

        :param code: The code of this ErrorPayload.
        :type: str
        """

        self._code = code

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
        if not isinstance(other, ErrorPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
