from __future__ import annotations

import pprint


class Operation(object):
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
        id=None,
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
        """Operation - a model defined in Swagger"""
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
        self.id = id
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
        """Gets the id of this Operation.

        :returns: The id of this Operation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Operation.

        :param str id: The id of this Operation.
        """
        if id is None:
            raise ValueError('Invalid value for `id`, must not be `None`')

        self._id = id

    @property
    def status(self):
        """Gets the status of this Operation.

        :returns: The status of this Operation.
        :rtype: clients.tinkoff.models.OperationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Operation.

        :param clients.tinkoff.models.OperationStatus status: The status of this Operation.
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def trades(self):
        """Gets the trades of this Operation.

        :returns: The trades of this Operation.
        :rtype: list[clients.tinkoff.models.OperationTrade]
        """
        return self._trades

    @trades.setter
    def trades(self, trades):
        """Sets the trades of this Operation.

        :param list[clients.tinkoff.models.OperationTrade] trades: The trades of this Operation.
        """

        self._trades = trades

    @property
    def commission(self):
        """Gets the commission of this Operation.

        :returns: The commission of this Operation.
        :rtype: clients.tinkoff.models.MoneyAmount
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this Operation.

        :param clients.tinkoff.models.MoneyAmount commission: The commission of this Operation.
        """

        self._commission = commission

    @property
    def currency(self):
        """Gets the currency of this Operation.

        :returns: The currency of this Operation.
                  clients.tinkoff.models.Currency
        :rtype: clients.tinkoff.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Operation.

        :param clients.tinkoff.models.Currency currency:
            The currency of this Operation.
        """
        if currency is None:
            raise ValueError(
                'Invalid value for `currency`, must not be `None`'
            )

        self._currency = currency

    @property
    def payment(self):
        """Gets the payment of this Operation.

        :returns: The payment of this Operation.
        :rtype: float
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Operation.

        :param float payment: The payment of this Operation.
        """
        if payment is None:
            raise ValueError('Invalid value for `payment`, must not be `None`')

        self._payment = payment

    @property
    def price(self):
        """Gets the price of this Operation.

        :returns: The price of this Operation.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Operation.

        :param float price: The price of this Operation.
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this Operation.

        Число инструментов в выставленной заявке
        :returns: The quantity of this Operation.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Operation.

        Число инструментов в выставленной заявке
        :param int quantity: The quantity of this Operation.
        """

        self._quantity = quantity

    @property
    def quantity_executed(self):
        """Gets the quantity_executed of this Operation.

        Число инструментов, исполненных в заявке
        :returns: The quantity_executed of this Operation.
        :rtype: int
        """
        return self._quantity_executed

    @quantity_executed.setter
    def quantity_executed(self, quantity_executed):
        """Sets the quantity_executed of this Operation.

        Число инструментов, исполненных в заявке
        :param int quantity_executed: The quantity_executed of this Operation.
        """

        self._quantity_executed = quantity_executed

    @property
    def figi(self):
        """Gets the figi of this Operation.

        :returns: The figi of this Operation.
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Operation.

        :param str figi: The figi of this Operation.
        """

        self._figi = figi

    @property
    def instrument_type(self):
        """Gets the instrument_type of this Operation.

        :returns: The instrument_type of this Operation.
        :rtype: clients.tinkoff.models.InstrumentType
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this Operation.

        :param clients.tinkoff.models.InstrumentType instrument_type:
            The instrument_type of this Operation.
        """

        self._instrument_type = instrument_type

    @property
    def is_margin_call(self):
        """Gets the is_margin_call of this Operation.

        :returns: The is_margin_call of this Operation.
        :rtype: bool
        """
        return self._is_margin_call

    @is_margin_call.setter
    def is_margin_call(self, is_margin_call):
        """Sets the is_margin_call of this Operation.

        :param bool is_margin_call: The is_margin_call of this Operation.
        """
        if is_margin_call is None:
            raise ValueError(
                'Invalid value for `is_margin_call`, must not be `None`'
            )

        self._is_margin_call = is_margin_call

    @property
    def _date(self):
        """Gets the _date of this Operation.

        ISO8601
        :returns: The _date of this Operation.
        :rtype: datetime.datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Operation.

        ISO8601
        :param datetime.datetime _date: The _date of this Operation.
        """
        if _date is None:
            raise ValueError('Invalid value for `_date`, must not be `None`')

        self.__date = _date

    @property
    def operation_type(self):
        """Gets the operation_type of this Operation.

        :returns: The operation_type of this Operation.
        :rtype: clients.tinkoff.models.OperationTypeWithCommission
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this Operation.

        :param clients.tinkoff.models.OperationTypeWithCommission operation_type:
            The operation_type of this Operation.
        """

        self._operation_type = operation_type

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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
