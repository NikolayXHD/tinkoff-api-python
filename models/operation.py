from __future__ import annotations

from . import _base


class Operation(_base.Model):
    swagger_types: dict[str, str] = {
        'id': 'str',
        'status': 'OperationStatus',
        'trades': 'list[OperationTrade]',
        'commission': 'MoneyAmount',
        'currency': 'Currency',
        'payment': 'float',
        'price': 'float',
        'quantity': 'int',
        'quantity_executed': 'int',
        'figi': 'str',
        'instrument_type': 'InstrumentType',
        'is_margin_call': 'bool',
        '_date': 'datetime',
        'operation_type': 'OperationTypeWithCommission',
    }

    attribute_map: dict[str, str] = {
        'id': 'id',
        'status': 'status',
        'trades': 'trades',
        'commission': 'commission',
        'currency': 'currency',
        'payment': 'payment',
        'price': 'price',
        'quantity': 'quantity',
        'quantity_executed': 'quantityExecuted',
        'figi': 'figi',
        'instrument_type': 'instrumentType',
        'is_margin_call': 'isMarginCall',
        '_date': 'date',
        'operation_type': 'operationType',
    }

    def __init__(
        self,
        op_id=None,
        status=None,
        trades=None,
        commission=None,
        currency=None,
        payment=None,
        price=None,
        quantity=None,
        quantity_executed=None,
        figi=None,
        instrument_type=None,
        is_margin_call=None,
        _date=None,
        operation_type=None,
    ):
        self._id = None
        self._status = None
        self._trades = None
        self._commission = None
        self._currency = None
        self._payment = None
        self._price = None
        self._quantity = None
        self._quantity_executed = None
        self._figi = None
        self._instrument_type = None
        self._is_margin_call = None
        self.__date = None
        self._operation_type = None
        self.discriminator = None
        self.id = op_id
        self.status = status
        if trades is not None:
            self.trades = trades
        if commission is not None:
            self.commission = commission
        self.currency = currency
        self.payment = payment
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if quantity_executed is not None:
            self.quantity_executed = quantity_executed
        if figi is not None:
            self.figi = figi
        if instrument_type is not None:
            self.instrument_type = instrument_type
        self.is_margin_call = is_margin_call
        self._date = _date
        if operation_type is not None:
            self.operation_type = operation_type

    @property
    def id(self):
        """
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, op_id):
        """
        :param str op_id:
        """
        if op_id is None:
            raise ValueError('Invalid value for `id`, must not be `None`')

        self._id = op_id

    @property
    def status(self):
        """
        :rtype: clients.tinkoff.models.OperationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param clients.tinkoff.models.OperationStatus status:
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def trades(self):
        """
        :rtype: list[clients.tinkoff.models.OperationTrade]
        """
        return self._trades

    @trades.setter
    def trades(self, trades):
        """
        :param list[clients.tinkoff.models.OperationTrade] trades:
        """
        self._trades = trades

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

    @property
    def currency(self):
        """
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        :param clients.tinkoff.models.Currency currency:
        """
        if currency is None:
            raise ValueError(
                'Invalid value for `currency`, must not be `None`'
            )

        self._currency = currency

    @property
    def payment(self):
        """
        :rtype: float
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """
        :param float payment:
        """
        if payment is None:
            raise ValueError('Invalid value for `payment`, must not be `None`')

        self._payment = payment

    @property
    def price(self):
        """
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        :param float price:
        """
        self._price = price

    @property
    def quantity(self):
        """
        Число инструментов в выставленной заявке
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Число инструментов в выставленной заявке
        :param int quantity:
        """
        self._quantity = quantity

    @property
    def quantity_executed(self):
        """
        Число инструментов, исполненных в заявке
        :rtype: int
        """
        return self._quantity_executed

    @quantity_executed.setter
    def quantity_executed(self, quantity_executed):
        """
        Число инструментов, исполненных в заявке
        :param int quantity_executed:
        """
        self._quantity_executed = quantity_executed

    @property
    def figi(self):
        """
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """
        :param str figi:
        """
        self._figi = figi

    @property
    def instrument_type(self):
        """
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """
        :param clients.tinkoff.models.InstrumentType instrument_type:

        """
        self._instrument_type = instrument_type

    @property
    def is_margin_call(self):
        """
        :rtype: bool
        """
        return self._is_margin_call

    @is_margin_call.setter
    def is_margin_call(self, is_margin_call):
        """
        :param bool is_margin_call:
        """
        if is_margin_call is None:
            raise ValueError(
                'Invalid value for `is_margin_call`, must not be `None`'
            )

        self._is_margin_call = is_margin_call

    @property
    def _date(self):
        """
        ISO8601
        :rtype: datetime.datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """
        ISO8601
        :param datetime.datetime _date:
        """
        if _date is None:
            raise ValueError('Invalid value for `_date`, must not be `None`')

        self.__date = _date

    @property
    def operation_type(self):
        """
        :rtype: clients.tinkoff.models.OperationTypeWithCommission
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, op_type):
        """
        :type clients.tinkoff.models.OperationTypeWithCommission op_type:
        """
        self._operation_type = op_type
