from __future__ import annotations

import pprint


class OrderbookResponse(object):
    swagger_types: dict[str, str] = {
        'tracking_id': 'str',
        'status': 'str',
        'payload': 'Orderbook',
    }

    attribute_map: dict[str, str] = {
        'tracking_id': 'trackingId',
        'status': 'status',
        'payload': 'payload',
    }

    def __init__(self, tracking_id=None, status='Ok', payload=None):
        """OrderbookResponse - a model defined in Swagger"""
        self._tracking_id = None
        self._status = None
        self._payload = None
        self.discriminator = None
        self.tracking_id = tracking_id
        self.status = status
        self.payload = payload

    @property
    def tracking_id(self):
        """Gets the tracking_id of this OrderbookResponse.

        :returns: The tracking_id of this OrderbookResponse.
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this OrderbookResponse.

        :param tracking_id: The tracking_id of this OrderbookResponse.
        :type: str
        """
        if tracking_id is None:
            raise ValueError(
                'Invalid value for `tracking_id`, must not be `None`'
            )

        self._tracking_id = tracking_id

    @property
    def status(self):
        """Gets the status of this OrderbookResponse.

        :returns: The status of this OrderbookResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderbookResponse.

        :param status: The status of this OrderbookResponse.
        :type: str
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def payload(self):
        """Gets the payload of this OrderbookResponse.

        :returns: The payload of this OrderbookResponse.
        :rtype: clients.tinkoff.models.Orderbook
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this OrderbookResponse.

        :param payload: The payload of this OrderbookResponse.
        :type: clients.tinkoff.models.Orderbook
        """
        if payload is None:
            raise ValueError('Invalid value for `payload`, must not be `None`')

        self._payload = payload

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
        if not isinstance(other, OrderbookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
