from __future__ import annotations

from . import _base


class PortfolioResponse(_base.Model):
    swagger_types: dict[str, str] = {
        'tracking_id': 'str',
        'status': 'str',
        'payload': 'Portfolio',
    }

    attribute_map: dict[str, str] = {
        'tracking_id': 'trackingId',
        'status': 'status',
        'payload': 'payload',
    }

    def __init__(self, tracking_id=None, status='Ok', payload=None):
        self._tracking_id = None
        self._status = None
        self._payload = None
        self.discriminator = None
        self.tracking_id = tracking_id
        self.status = status
        self.payload = payload

    @property
    def tracking_id(self):
        """
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """
        :param str tracking_id:
        """
        if tracking_id is None:
            raise ValueError(
                'Invalid value for `tracking_id`, must not be `None`'
            )

        self._tracking_id = tracking_id

    @property
    def status(self):
        """
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param str status:
        """
        if status is None:
            raise ValueError('Invalid value for `status`, must not be `None`')

        self._status = status

    @property
    def payload(self):
        """
        :rtype: clients.tinkoff.models.Portfolio
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        :param clients.tinkoff.models.Portfolio payload:
        """
        if payload is None:
            raise ValueError('Invalid value for `payload`, must not be `None`')

        self._payload = payload
