from __future__ import annotations

from . import _base


class ErrorPayload(_base.Model):
    swagger_types: dict[str, str] = {'message': 'str', 'code': 'str'}

    attribute_map: dict[str, str] = {'message': 'message', 'code': 'code'}

    def __init__(self, message=None, code=None):
        self._message = None
        self._code = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    @property
    def message(self):
        """
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        :param str message:
        """
        self._message = message

    @property
    def code(self):
        """
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        :param str code:
        """
        self._code = code
