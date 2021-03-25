from __future__ import annotations

import pprint


class PlacedLimitOrder(object):
    swagger_types: dict[str, str] = {
        'order_id': 'str',
        'operation': 'OperationType',
        'status': 'OrderStatus',
        'reject_reason': 'str',
        'message': 'str',
        'requested_lots': 'int',
        'executed_lots': 'int',
        'commission': 'MoneyAmount'
    }

    attribute_map: dict[str, str] = {
        'order_id': 'orderId',
        'operation': 'operation',
        'status': 'status',
        'reject_reason': 'rejectReason',
        'message': 'message',
        'requested_lots': 'requestedLots',
        'executed_lots': 'executedLots',
        'commission': 'commission'
    }

    def __init__(self, order_id=None, operation=None, status=None, reject_reason=None, message=None, requested_lots=None, executed_lots=None, commission=None):
        """PlacedLimitOrder - a model defined in Swagger"""
        self._order_id = None
        self._operation = None
        self._status = None
        self._reject_reason = None
        self._message = None
        self._requested_lots = None
        self._executed_lots = None
        self._commission = None
        self.discriminator = None
        self.order_id = order_id
        self.operation = operation
        self.status = status
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if message is not None:
            self.message = message
        self.requested_lots = requested_lots
        self.executed_lots = executed_lots
        if commission is not None:
            self.commission = commission

    @property
    def order_id(self):
        """Gets the order_id of this PlacedLimitOrder.

        :returns: The order_id of this PlacedLimitOrder.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PlacedLimitOrder.

        :param order_id: The order_id of this PlacedLimitOrder.
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")

        self._order_id = order_id

    @property
    def operation(self):
        """Gets the operation of this PlacedLimitOrder.

        :returns: The operation of this PlacedLimitOrder.
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PlacedLimitOrder.

        :param operation: The operation of this PlacedLimitOrder.
        :type operation: clients.tinkoff.models.OperationType
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")

        self._operation = operation

    @property
    def status(self):
        """Gets the status of this PlacedLimitOrder.

        :returns: The status of this PlacedLimitOrder.
        :rtype: clients.tinkoff.models.OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlacedLimitOrder.

        :param status: The status of this PlacedLimitOrder.
        :type: clients.tinkoff.models.OrderStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def reject_reason(self):
        """Gets the reject_reason of this PlacedLimitOrder.

        :returns: The reject_reason of this PlacedLimitOrder.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this PlacedLimitOrder.

        :param reject_reason: The reject_reason of this PlacedLimitOrder.
        :type: str
        """

        self._reject_reason = reject_reason

    @property
    def message(self):
        """Gets the message of this PlacedLimitOrder.

        Сообщение об ошибке
        :returns: The message of this PlacedLimitOrder.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PlacedLimitOrder.

        Сообщение об ошибке
        :param message: The message of this PlacedLimitOrder.
        :type: str
        """

        self._message = message

    @property
    def requested_lots(self):
        """Gets the requested_lots of this PlacedLimitOrder.

        :returns: The requested_lots of this PlacedLimitOrder.
        :rtype: int
        """
        return self._requested_lots

    @requested_lots.setter
    def requested_lots(self, requested_lots):
        """Sets the requested_lots of this PlacedLimitOrder.

        :param requested_lots: The requested_lots of this PlacedLimitOrder.
        :type: int
        """
        if requested_lots is None:
            raise ValueError("Invalid value for `requested_lots`, must not be `None`")

        self._requested_lots = requested_lots

    @property
    def executed_lots(self):
        """Gets the executed_lots of this PlacedLimitOrder.

        :returns: The executed_lots of this PlacedLimitOrder.
        :rtype: int
        """
        return self._executed_lots

    @executed_lots.setter
    def executed_lots(self, executed_lots):
        """Sets the executed_lots of this PlacedLimitOrder.

        :param executed_lots: The executed_lots of this PlacedLimitOrder.
        :type: int
        """
        if executed_lots is None:
            raise ValueError("Invalid value for `executed_lots`, must not be `None`")

        self._executed_lots = executed_lots

    @property
    def commission(self):
        """Gets the commission of this PlacedLimitOrder.

        :returns: The commission of this PlacedLimitOrder.
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this PlacedLimitOrder.

        :param commission: The commission of this PlacedLimitOrder.
        :type: clients.tinkoff.models.MoneyAmount
        """

        self._commission = commission

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
        if not isinstance(other, PlacedLimitOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
