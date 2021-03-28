from __future__ import annotations

from . import _base


class PlacedLimitOrder(_base.Model):
    swagger_types: dict[str, str] = {
        'order_id': 'str',
        'operation': 'OperationType',
        'status': 'OrderStatus',
        'reject_reason': 'str',
        'message': 'str',
        'requested_lots': 'int',
        'executed_lots': 'int',
        'commission': 'MoneyAmount',
    }

    attribute_map: dict[str, str] = {
        'order_id': 'orderId',
        'operation': 'operation',
        'status': 'status',
        'reject_reason': 'rejectReason',
        'message': 'message',
        'requested_lots': 'requestedLots',
        'executed_lots': 'executedLots',
        'commission': 'commission',
    }

    def __init__(
        self,
        order_id=None,
        operation=None,
        status=None,
        reject_reason=None,
        message=None,
        requested_lots=None,
        executed_lots=None,
        commission=None,
    ):
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
        """
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        :param str order_id:
        """
        if order_id is None:
            raise ValueError(
                'Invalid value for `order_id`, must not be `None`'
            )

        self._order_id = order_id

    @property
    def operation(self):
        """
        :rtype: clients.tinkoff.models.OperationType
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        :param clients.tinkoff.models.OperationType operation:
        """
        if operation is None:
            raise ValueError(
                'Invalid value for `operation`, must not be `None`'
            )

        self._operation = operation

    @property
    def status(self):
        """
        :rtype: clients.tinkoff.models.OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param clients.tinkoff.models.OrderStatus status:
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def reject_reason(self):
        """
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """
        :param str reject_reason:
        """
        self._reject_reason = reject_reason

    @property
    def message(self):
        """
        Сообщение об ошибке
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Сообщение об ошибке
        :param str message:
        """
        self._message = message

    @property
    def requested_lots(self):
        """
        :rtype: int
        """
        return self._requested_lots

    @requested_lots.setter
    def requested_lots(self, requested_lots):
        """
        :param int requested_lots:
        """
        if requested_lots is None:
            raise ValueError(
                'Invalid value for `requested_lots`, must not be `None`'
            )

        self._requested_lots = requested_lots

    @property
    def executed_lots(self):
        """
        :rtype: int
        """
        return self._executed_lots

    @executed_lots.setter
    def executed_lots(self, executed_lots):
        """
        :param int executed_lots:
        """
        if executed_lots is None:
            raise ValueError(
                'Invalid value for `executed_lots`, must not be `None`'
            )

        self._executed_lots = executed_lots

    @property
    def commission(self):
        """
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """
        :param clients.tinkoff.models.MoneyAmount commission:
        """
        self._commission = commission
